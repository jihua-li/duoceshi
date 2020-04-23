import pytest,logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s-%(levelname)s-%(message)s')

# @pytest_frame.mark.usefixtures("login")
class Testcase():
    def test_01(self, login):
        l = login
        logging.info("class test case1, 返回值为：{}".format(l))
    def test_02(self, login):
        l = login
        logging.info("class test case2, 返回值为：{}".format(l))