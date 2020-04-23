from tsms_project.commons.tsms_base import Tsmstest
from tsms_project.commons.tsms_redis import TsmsRedis
from tsms_project.commons.tsms_db import OperationDb
import unittest, logging, random


class Charge(unittest.TestCase):
    '''充值'''
    @classmethod
    def setUpClass(cls):
        cls.ts = Tsmstest()
        cls.tr = TsmsRedis()
        cls.od = OperationDb()
    @classmethod
    def tearDownClass(cls):
        pass
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_charge_success(self):
        '''充值成功操作'''
        charge = random.randint(100,200)
        user = 'lijihua'
        data = {
            "user": user,
            "charge": charge
        }
        #查询充值前金额
        fist_money = self.tr.get_account(user)
        logging.info("充值前金额为：{}".format(fist_money))
        #充值
        self.ts.req_post('charge', data, 'root', '123')
        # print(self.ts.status_code, self.ts.text)
        assert self.ts.status_code == 200
        assert self.ts.text == 'ok'
        #查询充值后金额
        last_money = self.tr.get_account(user)
        logging.info("充值后金额为：{}".format(last_money))
        if fist_money == None:
            assert last_money == charge

        else:
            assert last_money == fist_money + charge

if __name__ =='__main__':
    unittest.main()



