import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s-%(levelname)s-%(message)s')


def test_01(login):
    l = login
    logging.info("function test case1, 返回值为：{}".format(l))