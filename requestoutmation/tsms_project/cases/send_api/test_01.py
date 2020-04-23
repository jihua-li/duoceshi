from tsms_project.commons.tsms_base import Tsmstest
from tsms_project.commons.tsms_decorator import logit
import unittest, logging
from tenacity import retry, stop_after_attempt, wait_exponential
from tsms_project.commons.tsms_web import TsmsWeb


class SendMessage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ts = Tsmstest()
        cls.tw = TsmsWeb()
        logging.info("start")
        cls.tw.login('lijihua', 'lijihua198915')
        logging.info("end")
        assert cls.tw.is_login('lijihua'), "登录失败"
        # # 登录tsms
        # cls.tw.login('lijihua', 'lijihua198915')
        # logging.info("end")
        # assert cls.tw.is_login('lijihua'), "登录失败"

    @classmethod
    def tearDownClass(cls):
        pass

    # @retry(stop_after_attempt(3), wait=wait_exponential(multiplier=1, max=10))  # 错误重试机制
    # def check_web(self, phone):
    #     '''检查页面展示数据发送号码，发送状态，消耗条数数据是否正确'''
    #     logging.info("ok")
    #     res_list = self.tw.reg_send('lijihua')
    #     end_res = self.tw.get_res(phone, res_list)
    #     createtime, phonenumble, message, status, consumption = end_res[0], end_res[1], end_res[2], end_res[3], \
    #                                                             end_res[4]
    #     assert status == 'success', "发送信息失败{}".format(status)
    #     assert consumption == 1

    def test_send_message_success(self):
        '''短信发送成功'''
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
        # 请求发送信息接口
        self.ts.req_post('message', data9, 'lijihua', 'lijihua198915')
        assert self.ts.status_code == 200
        assert isinstance(self.ts.json['uuid'], str), "发送信息接口请求失败"

        # 查前端
        # self.check_web(phone[0])
        # 登录tsms
        # self.tw.login('lijihua', 'lijihua198915')
        # logging.info("end")
        # assert self.tw.is_login('lijihua'), "登录失败"
        logging.info("ok")
        res_list = self.tw.reg_send('lijihua')
        end_res = self.tw.get_res(phone, res_list)
        createtime, phonenumble, message, status, consumption = end_res[0], end_res[1], end_res[2], end_res[3], \
                                                                end_res[4]
        assert status == 'success', "发送信息失败{}".format(status)
        assert consumption == 1



if __name__ == '__main__':
    unittest.main()
