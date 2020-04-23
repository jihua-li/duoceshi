from tsms_project.commons.tsms_base import Tsmstest
from tsms_project.commons.tsms_decorator import logit
import logging,unittest

logging.basicConfig(level=logging.INFO, format=('%(asctime)-16s %(levelname)-8s %(message)s'))

class CreateTemp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        '''请求数据'''
        cls.ts = Tsmstest()
        module = cls.ts.gen_ranstr(3, 3)
        sign_id = 114
        cls.data = {
            "name": module,
            "template": '模版内容',
            "type": 1,
            "description": '我要申请模版',
            "sign_id": sign_id
        }
    @classmethod
    def tearDownClass(cls):
        pass
    def setUp(self):
        pass
    def tearDown(self):
        pass

    @logit
    def test_create_temp_success(self):
        '''
        创建模版成功
        :param data: 请求数据
        :return: 成功无返回数据
        '''
        self.ts.req_post('temp', self.data)
        assert self.ts.status_code == 200
        assert isinstance(self.ts.json['temp_id'], int), "创建模版失败"

    def test_create_temp_fail(self):
        '''
        创建模版失败，账号错误
        :param data: 请求数据
        :return: 用例通过则无返回
        '''
        self.ts.req_post('temp', self.data, user='lijihua')
        assert self.ts.status_code == 400
        assert self.ts.json['message'] == 'auth not pass', "创建模版失败接口返回内容不正确"


if __name__=='__main__':
    unittest.main()
