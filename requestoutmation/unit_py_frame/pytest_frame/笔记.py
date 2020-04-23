'''
重点：
1。fixture测试夹具，参数scop决定作用域
pytest.fixture(scop="")
2.conftest统一管理
3.前置后置
4.强制后置
5.
6.
'''

import logging,pytest

logging.basicConfig(level=logging.INFO, format='%(asctime)16s - %(levelname)8s - %(message)s')

a = 'test_input,expected'
b = [
    ("1+2", 3),
    ("2*3", 6),
    pytest.param("3-0", 3, marks=pytest.mark.xfail),
]

@pytest.mark.parametrize(a, b)
def test_eval(test_input, expected):
    logging.info("执行测试用例")
    assert eval(test_input) == expected
    logging.info(test_input)
    logging.info(expected)
