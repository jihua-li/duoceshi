import pytest, logging

logging.basicConfig(level=logging.INFO, format='%(acstime)s-%(levelname)s-%(message)s')

'''@pytest_frame.mark.parametrize("login", test_login_data, indirect=True) 
接收三个参 数:
～字符串，和前置函数的名称一致
～测试数据组 
～indirect=True，标识第一个参数是函数名，而不是字符 '''

"""pytest.mark.parametrize()基本用法"""
test_login_data1 = {
    ('root', '123'),
    ('admin', 'admin'),
    ('dsc', '123'),
}

def login(user, pwd):
    logging.info(user)
    logging.info(pwd)
    return user, pwd

@pytest.mark.level1
@pytest.mark.parametrize("user,pwd", test_login_data1)
def test_login1(user, pwd):
    result = login(user, pwd)
    logging.info(result)
    logging.info('ok')

"""结合fixture"""
#测试数据组中元素为元组
test_login_data2 = {
    ('root', '123'),
    ('admin', 'admin'),
    ('dsc', '123'),
}

@pytest.fixture(scope='function')
def login2(request):
    user, pwd = request.param
    logging.info(user)
    logging.info(pwd)
    return user, pwd

@pytest.mark.level2
@pytest.mark.parametrize("login2", test_login_data2, indirect=True)
def test_login2(login2):
    logging.info("夹具login返回的结果是：{}".format(login2))
    logging.info('ok')

#测试数据组中元素为字典
test_login_data3 = [
        {"user": "dcs", "psw": "123"},
        {"user": "root", "psw": "1234"},
        {"user": "carl", "psw": "12345"},
]


@pytest.fixture(scope='function')
def login3(request):
    user = request.param['user']
    pwd = request.param['psw']
    logging.info(user)
    logging.info(pwd)
    return user, pwd

@pytest.mark.level3
@pytest.mark.parametrize("login3", test_login_data3, indirect=True)
def test_login(login3):
    logging.info("夹具login3返回的结果是: {}".format(login3))
    logging.info('ok')


'''练习：
使用mark.parametrize装饰器实现数据驱动，完成多组数据计算：[ ("1+1", 2), ("2*3", 6), ("3-1", 1),] 和断言'''

test_data = [
    ("1+1", 2),
    ("2*3", 6),
    ("3-1", 1),
]

@pytest.mark.parametrize("test_input,expected", test_data)
def test_eval(test_input, expected):
    logging.info(test_input, expected)
    assert eval(test_input) == expected


@pytest.fixture(scope='function')
def add(request):
    a, b = request.param
    logging.info(a)
    logging.info(b)
    return a, b

@pytest.mark.parametrize("add", test_data, indirect=True)
def test_add(add):
    a, b = add
    logging.info(add)
    assert eval(a) == b