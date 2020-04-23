from tsms_project.commons.tsms_base import Tsmstest
from tsms_project.commons.tsms_decorator import logit
import unittest, logging, random, ddt
from tenacity import retry, stop_after_attempt, wait_exponential
from tsms_project.commons.tsms_web import TsmsWeb
from tsms_project.commons.tsms_db import OperationDb
from tsms_project.commons.tsms_redis import TsmsRedis


class SendMessage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ts = Tsmstest()
        cls.tw = TsmsWeb()
        cls.tr = TsmsRedis()
        cls.opr_db = OperationDb()
        cls.user = 'lijihua'
        cls.password = 'lijihua198915'
        # 调取随机生成手机号方法生成手机号码
        cls.phone = cls.ts.gen_phones(1)
        # 登录tsms
        # cls.tw.login('lijihua', 'lijihua198915')
        # assert cls.tw.is_login('lijihua'), "登录失败"

    @classmethod
    def tearDownClass(cls):
        pass
    def setUp(self):
        # 调取随机生成手机号方法生成手机号码
        self.phone = self.ts.gen_phones(1)

    @retry(stop=stop_after_attempt(5), wait=wait_exponential(multiplier=1, max=10))
    def check_db(self, phone):
        db_res = self.opr_db.tsms_select("sms_send", "mobile,status,consume",uuid=self.ts.json["uuid"])[0]
        assert db_res['mobile'] == phone
        assert db_res['status'] == 'success'
        assert db_res['consume'] == 1


    def test_send_01(self):
        '''短信发送成功,检查redis金额和记频,检查数据库状态'''
        # #测试账号密码
        # user = self.user
        # password = self.password
        # #调取随机生成手机号方法生成手机号码
        # phone = self.phone

        #获取发送信息前金额及频率
        fist_money = self.tr.get_account(self.user)
        logging.info("fist_money:{}".format(fist_money))
        # fist_freq, fist_freq_ttl = self.tr.get_freq(phone)
        # logging.info("fist_freq:{},fist_freq_ttl:{}".format(fist_freq,fist_freq_ttl))

        # 查询审批通过的sign_id
        self.ts.tsms_get('sign', self.user, self.password)
        sign_id = self.ts.get_field('id', audit_status='passed')
        # #查询审批通过的sign_id下的审批通过的temp_id
        self.ts.tsms_get('temp', self.user, self.password)
        temp_id = self.ts.get_field('id', audit_status='passed', sign_id=sign_id)

        data9 = {
            "sign_id": sign_id,
            "temp_id": temp_id,
            "mobiles": self.phone
        }
        # 请求发送信息接口
        self.ts.req_post('message', data9, self.user, self.password)
        assert self.ts.status_code == 200
        assert isinstance(self.ts.json['uuid'], str), "发送信息接口请求失败"

        #获取发送信息后金额和频率
        now_money = self.tr.get_account(self.user)
        now_freq, last_freq_ttl = self.tr.get_freq(self.phone[0])

        assert now_money == fist_money - 1
        assert now_freq == 1
        assert 599 <= last_freq_ttl <=600

        #检查数据库
        self.check_db(self.phone[0])


    @retry(stop=stop_after_attempt(5), wait=wait_exponential(multiplier=1, max=10))
    def check_db_freq_over(self, phone):
        db_res = self.opr_db.tsms_select('sms_send', "mobile,status,consume",uuid=self.ts.json["uuid"])[0]
        assert db_res['mobile'] == phone
        assert db_res['consume'] == 1
        assert db_res['status']  == 'over_freq'

    def test_send_02(self):
        '''验证超频边界值是否为20次'''

        #获取发送信息前金额及频率
        fist_money = self.tr.get_account(self.user)
        logging.info("fist_money:{}".format(fist_money))

        # 查询审批通过的sign_id
        self.ts.tsms_get('sign', self.user, self.password)
        sign_id = self.ts.get_field('id', audit_status='passed')
        # #查询审批通过的sign_id下的审批通过的temp_id
        self.ts.tsms_get('temp', self.user, self.password)
        temp_id = self.ts.get_field('id', audit_status='passed', sign_id=sign_id)

        data9 = {
            "sign_id": sign_id,
            "temp_id": temp_id,
            "mobiles": self.phone
        }
        # 请求发送信息接口
        self.ts.req_post('message', data9, self.user, self.password)
        assert self.ts.status_code == 200
        assert isinstance(self.ts.json['uuid'], str), "发送信息接口请求失败"

        #检查redis金额
        now_money = self.tr.get_account(self.user)
        #检查金额计费是否准确
        assert now_money == fist_money - 1
        freq, ttl = self.tr.get_freq(self.phone[0])
        assert freq == 1
        assert 599 <= ttl <= 600

        #更新用户频次为临界值19
        freq_res = self.tr.set_freq(self.phone[0], 600, 19)
        assert freq_res == 19

        #第一次发送（成功）
        self.ts.req_post('message', data9, self.user, self.password)
        assert self.ts.status_code == 200
        assert isinstance(self.ts.json['uuid'], str), "短信发送接口请求失败"

        #第二次发送（超频）
        self.ts.req_post('message', data9, self.user, self.password)
        assert self.ts.status_code == 403
        # assert self.ts.json == "{'error': 'ER:0036', 'message': 'send freq out of limit'}"

        #将超频次数恢复成初始值
        self.tr.set_freq(self.phone, 600, 1)

        #检查数据库status字段值是否为over_freq, 目前因为超频时接口没有返回uuid导致无法查询数据库数据
        # self.check_db_freq_over(phone[0])


    def test_send_03(self):
        '''余额不足测试'''
        #查询初始金额
        fist_money = self.tr.get_account(self.user)

        #将金额修改为0
        self.tr.set_account(self.user, 0)
        try:
            # 查询审批通过的sign_id
            self.ts.tsms_get('sign', self.user, self.password)
            sign_id = self.ts.get_field('id', audit_status='passed')
            # #查询审批通过的sign_id下的审批通过的temp_id
            self.ts.tsms_get('temp', self.user, self.password)
            temp_id = self.ts.get_field('id', audit_status='passed', sign_id=sign_id)

            data9 = {
                "sign_id": sign_id,
                "temp_id": temp_id,
                "mobiles": self.phone
            }
            # 请求发送信息接口
            self.ts.req_post('message', data9, self.user, self.password)
            assert self.ts.status_code == 403
            # assert self.ts.json == "{'error': 'ER:0035', 'message': 'message charge failed'}"
        except:
            raise
        finally:
            #回复初始金额
            self.tr.set_account(self.user, fist_money)






if __name__ =='__main__':
    unittest.main()