from tsms.tsms_base import Tsmstest
import requests, unittest, logging

logging.basicConfig(level=logging.INFO, format='%(asctime)-16s %(levelname)-8s %(message)s')

class SignAdd(unittest.TestCase):
    '''创建签名测试用例组'''
    #套件前置，所有用例执行前执行一次
    @classmethod
    def setUpClass(cls):
        ''''''
        pass
    #套件后置，所有用例执行后执行一次
    @classmethod
    def tearDownClass(cls):
        ''''''
        pass

    #用例前置，每一条执行前执行一次
    @classmethod
    def setUp(self):
        '''实例化测试库，全局引用'''
        self.ts = Tsmstest()
        '''创建签名成功'''
        data1 = {
            "signature": "haha",
            "source": "shenzhen",
            "pics": ["cc"]
        }
        self.new_sign_id_dict = self.ts.req_post('sign', data1)
        assert self.ts.status_code == 200
        assert isinstance(self.ts.json['sign_id'], int), "创建签名失败"

    #用例后置，每条用例执行完成后执行一次
    @classmethod
    def tearDown(self):
        '''清除测试数据'''
        try:
            if self.ts.status_code != 200:
                logging.info('----->{}'.format(self.ts.json))
                logging.info('数据删除开始:{}'.format(self.new_sign_id_dict))
                self.ts.req_del('sign', self.new_sign_id_dict)
            else:
                logging.info("=====数据不存在, 无需再次删除=====")
        except:
            logging.error('删除失败')
        # try:
        #     self.ts.req_del('sign', self.new_sign_id_dict)
        # except:
        #     logging.error('删除失败')


            # assert self.ts.status_code == 200


    def test1(self):
        '''删除签名成功'''
        self.ts.req_del('sign', self.ts.json)
        assert self.ts.status_code == requests.codes.ok


    def test2(self):
        '''删除签名失败'''
        self.ts.req_del('sign', self.ts.json, passwd='lijihua')
        assert self.ts.status_code == 400



if __name__ =='__main__':
    SignAdd.main()

