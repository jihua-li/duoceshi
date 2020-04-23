#1.unittest测试框架
import unittest
class RunTestCase(unittest.TestCase):
    # 套件前置，所有用例执行前执行一次
    @classmethod
    def setUpClass(cls):
        ''''''
        pass

    # 套件后置，所有用例执行后执行一次
    def tearDownClass(cls):
        ''''''
        pass

    # 用例前置，每一条执行前执行一次
    @classmethod
    def setUp(self):
        pass

    # 用例后置，每条用例执行完成后执行一次
    def tearDown(self):
        pass

    #测试用例1
    def test1(self):
        pass
    #测试用例2
    def test2(self):
        pass
