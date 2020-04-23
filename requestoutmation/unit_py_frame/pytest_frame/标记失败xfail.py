import pytest, logging

logging.basicConfig(level=logging.INFO, format='%(acstime)s-%(levelname)s-%(message)s')

"""标记失败
   @pytest.mark.xfail
   通过 marks=pytest.mark.xfail 标记失败，则该场景不运行"""

a = "test_input,expected"
b = [
    ("1+1", 2),
    ("2*3", 6),
    pytest.param("3-0", 1, marks=pytest.mark.xfail),
]

@pytest.mark.parametrize(a, b)
def test_eval1(test_input, expected):
    logging.info(test_input, expected)
    assert eval(test_input) == expected


"""参数组合，
     嵌套装饰器可以实现参数组合"""
@pytest.mark.parametrize('c', [None, 1, "c"])
@pytest.mark.parametrize('d', [None, 2, "d"])
def test_01(c, d):
    logging.info("执行测试用例 {} {}".format(c, d))
    assert c == d