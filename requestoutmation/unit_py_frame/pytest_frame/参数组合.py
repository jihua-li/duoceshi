import pytest, logging

logging.basicConfig(level=logging.INFO, format='%(acstime)s-%(levelname)s-%(message)s')


"""参数组合，
     嵌套装饰器可以实现参数组合"""
@pytest.mark.parametrize('c', [None, 1, "c"])
@pytest.mark.parametrize('d', [None, 2, "d"])
def test_01(c, d):
    logging.info("执行测试用例 {} {}".format(c, d))
    assert c == d