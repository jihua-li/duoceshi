from tsms_project.commons.tsms_base import Tsmstest
from tsms_project.commons.tsms_web import TsmsWeb
from tsms_project.commons.tsms_decorator import logit
import logging,unittest, requests
from tsms_project.commons.tsms_db import OperationDb

logging.basicConfig(level=logging.INFO, format=('%(asctime)-16s %(levelname)-8s %(message)s'))
# ts = Tsmstest()

class CreateSign(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ts = Tsmstest()
        cls.tw = TsmsWeb()
        cls.opr_db = OperationDb()
        cls.s = requests.session()
        cls.signature = cls.ts.gen_ranstr(num_letters=5)
        cls.data = {
            "signature": cls.signature,
            "source": "shenzhen",
            "pics": ["cc"]
        }

    @classmethod
    def tearDownClass(cls):
        pass
    def setUp(self):
        pass
    def tearDown(self):
        if "sign_id" in self.ts.json["sign_id"]:
            self.opr_db.tsms_record_del("sms_sign", sign_id = self.ts.json["sign_id"])

    def test_create_sign_success(self):
        '''创建签名成功'''
        '''创建签名接口正常用例'''
        self.ts.req_post('sign',self.data)
        assert self.ts.status_code == 200, '接口验证失败'
        assert isinstance(self.ts.json['sign_id'], int), '签名id类型有误'

    def test_create_sign_fail(self):
        '''创建签名失败，密码错误'''
        self.ts.req_post('sign', self.data, user = 'lijihua', passwd='lijihua198916')
        assert self.ts.status_code == 400, '接口验证失败'
        assert self.ts.json['message'] == 'auth not pass', '接口返回参数异常'

    def test_create_verify_sign(self):
        '''创建一个随机签名，再从前端获取该签名id的内容，然后判断：签名id/签名内容/审核状态是否准确'''
        #先创建一个随机签名, 并获取到该签名的id
        self.ts.req_post('sign',self.data)
        # sign_id = self.ts.json['sign_id']

        #判断签名id/签名内容/审核状态是否准确
        self.tw.login('lijihua')
        assert self.tw.is_login()
        res = self.tw.reg_sign()
        create_time,sign_id,sign_name,status = self.tw.get_res(self.ts.json['sign_id'], res)

        #断言
        assert sign_id == str(self.ts.json['sign_id'])
        assert sign_name == self.signature
        assert status == 'reviewing'


    def test_create_sign_assert_to_db(self):
        '''创建一个随机签名，再从数据库获取该签名id的内容，然后判断：签名id/签名内容/审核状态是否准确'''
        # 先创建一个随机签名, 并获取到该签名的id
        self.ts.req_post('sign', self.data, 'lijihua')

        #查询数据库是否包含接口返回sign_id的相关信息
        res = self.opr_db.tsms_select('sms_sign','*', sign_id =self.ts.json['sign_id'])
        assert self.signature == res[0]['signature']
        assert 'reviewing' == res[0]['audit_status']

if __name__=='__main__':
    unittest.main()
