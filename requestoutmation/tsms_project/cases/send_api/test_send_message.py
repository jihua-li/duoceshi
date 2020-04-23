from tsms_project.commons.tsms_base import Tsmstest
from tsms_project.commons.tsms_decorator import logit
import unittest, logging, random
from tenacity import retry, stop_after_attempt, wait_exponential
from tsms_project.commons.tsms_web import TsmsWeb
from tsms_project.commons.tsms_db import OperationDb


class SendMessage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.ts = Tsmstest()
        cls.tw = TsmsWeb()
        cls.opr_db = OperationDb()
        # 登录tsms
        # cls.tw.login('carl', 'lijihua198915')
        # assert cls.tw.is_login('carl'), "登录失败"



    @classmethod
    def tearDownClass(cls):
        pass

    def test_send_message(self):
        '''短信发送成功'''
        # 查询审批通过的sign_id
        self.ts.tsms_get('sign')
        # print(ts.json)
        sign_id = self.ts.get_field('id', audit_status='passed')
        # print(sign_id)
        # #查询审批通过的sign_id下的审批通过的temp_id
        self.ts.tsms_get('temp')
        temp_id = self.ts.get_field('id', audit_status='passed', sign_id= sign_id)
        # print(temp_id)
        # #调取随机生成手机号方法生成手机号码
        phone = self.ts.gen_phones(1)
        # print(phone)

        data9 = {
            "sign_id": sign_id,
            "temp_id": temp_id,
            "mobiles": phone
            }
        self.ts.req_post('message', data9)
        assert self.ts.status_code == 200
        assert isinstance(self.ts.json['uuid'], str), "短信发送接口请求失败"


    def test_send_message_overclocking(self):
        '''短信发送成功且超频'''
        # 查询审批通过的sign_id
        self.ts.tsms_get('sign', 'lijihua', 'lijihua198915')
        # print(ts.json)
        sign_id = self.ts.get_field('id', audit_status='passed')
        # print(sign_id)
        # #查询审批通过的sign_id下的审批通过的temp_id
        self.ts.tsms_get('temp', 'lijihua', 'lijihua198915')
        temp_id = self.ts.get_field('id', audit_status='passed', sign_id=sign_id)
        # print(temp_id)
        # #调取随机生成手机号方法生成手机号码
        phone = self.ts.gen_phones(1)
        # print(phone)

        # 测试超频，发送信息结果执行20次
        i = 20
        for x in range(i):
            data9 = {
                "sign_id": sign_id,
                "temp_id": temp_id,
                "mobiles": phone
            }
            self.ts.req_post('message', data9, 'lijihua', 'lijihua198915')
            assert self.ts.status_code == 200
            assert isinstance(self.ts.json['uuid'], str), "短信发送接口请求失败"
            i -= 1

    @retry(stop=stop_after_attempt(10), wait=wait_exponential(multiplier=1, max=10)) #错误重试机制
    def check_web(self, phone):
        '''检查页面展示数据发送号码，发送状态，消耗条数数据是否正确'''
        res_list = self.tw.reg_send('lijihua')
        end_res = self.tw.get_res(phone, res_list)
        createtime, phonenumble, message, status, consumption = end_res[0], end_res[1], end_res[2], end_res[3], \
                                                                end_res[4]
        print(status,type(status))
        assert status == 'success', "发送信息失败，期待返回{}，实际返回{}".format("success", status)
        assert int(consumption) == 1, "消耗条数不正确"

    def test_send_message_success(self):
        '''短信发送成功,并检查数据状态是否会变成success，通过错误重试去获取最终异步处理的结果'''
        # 查询审批通过的sign_id
        self.ts.tsms_get('sign', 'lijihua', 'lijihua198915')
        sign_id = self.ts.get_field('id', audit_status='passed')
        # #查询审批通过的sign_id下的审批通过的temp_id
        self.ts.tsms_get('temp', 'lijihua', 'lijihua198915')
        temp_id = self.ts.get_field('id', audit_status='passed', sign_id=sign_id)
        # #调取随机生成手机号方法生成手机号码
        phone = self.ts.gen_phones(1)

        data9 = {
            "sign_id": sign_id,
            "temp_id": temp_id,
            "mobiles": phone
        }
        #请求发送信息接口
        self.ts.req_post('message', data9, 'lijihua', 'lijihua198915')
        assert self.ts.status_code == 200
        assert isinstance(self.ts.json['uuid'], str), "发送信息接口请求失败"

        #查前端
        self.check_web(phone[0])

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def get_sign_name(self, sign_id):
        '''从数据库查询签名内容'''
        res = self.opr_db.tsms_select('sms_sign', 'signature', sign_id=sign_id)
        logging.info("[查询签名的内容为]：{}".format(res))
        signature = res[0]['signature']
        return signature

    def get_temp_name(self, temp_id):
        '''从数据库查询模版内容'''
        res = self.opr_db.tsms_select('sms_template', 'template', temp_id=temp_id)
        logging.info("[查询模版的内容为]：{}".format(res))
        return res[0]['template']

    def get_send_content(self, sign_id, temp_id):
        '''合并签名，模版内容'''
        sign_name = self.get_sign_name(sign_id)
        temp_name = self.get_temp_name(temp_id)
        content = '【{}】{}'.format(sign_name,temp_name)
        logging.info("[content内容为]：{}".format(content))
        return content



    @retry(stop = stop_after_attempt(5), wait = wait_exponential(multiplier=1, max=10)) #错误重试机制
    def check_send_ok(self, sign_id, temp_id, uuid):
        '''断言数据库结果'''
        send_res = self.opr_db.tsms_select('sms_send', '*', sign_id=sign_id, temp_id=temp_id, uuid=uuid)
        print(send_res)
        assert send_res[0]['status'] == 'success'
        assert send_res[0]['consume'] == 1
        assert send_res[0]['content'] == self.get_send_content(sign_id, temp_id)


    def test_send_message_check_to_db(self):
        '''短信发送成功，断言数据库数据正确'''
        #查询审批通过的sign_id
        sign_ids = self.opr_db.tsms_select('sms_sign', 'sign_id', audit_status='passed', sign_user_id = 16)
        sign_id_list =[]
        for s in sign_ids:
            sign_id_list.append(s['sign_id'])

        #查询审批通过的sign_id下的审批通过的temp_id
        temp_id_list = []
        #把找到的符合条件的temp_id添加到temp_id_list中
        for sign_id in sign_id_list:
            res = self.opr_db.tsms_select('sms_template','temp_id', temp_sign_id = sign_id,audit_status='passed')
            if res:
                temp_id_list.append(res[0]['temp_id'])
        #随机取一个temp_id
        temp_id = random.choice(temp_id_list)
        # print(temp_id)
        #通过temp_id反查sign_id
        res = self.opr_db.tsms_select('sms_template','temp_sign_id', temp_id = temp_id)
        sign_id = res[0]['temp_sign_id']
        #调取随机生成手机号方法生成手机号码
        phone = self.ts.gen_phones(1)
        #定义接口请求参数
        data9 = {
            "sign_id": sign_id,
            "temp_id": temp_id,
            "mobiles": phone
        }
        # 请求发送信息接口
        self.ts.req_post('message', data9, 'carl', 'lijihua198915')
        assert self.ts.status_code == 200
        assert isinstance(self.ts.json['uuid'], str), "发送信息接口请求失败"


        #校验数据库
        self.check_send_ok(sign_id, temp_id,self.ts.json['uuid'])
        #断言数据库结果
        # send_res = self.opr_db.tsms_select('sms_send', '*', sign_id = sign_id, temp_id = temp_id, uuid = self.ts.json['uuid'])
        # print(send_res)
        # assert send_res[0]['status'] == 'seccess'
        # assert send_res[0]['consume'] == 1





if __name__ =='__main__':
    unittest.main()