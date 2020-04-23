import pytest,logging
from test_tsms_pytest_project.pytest_commons.tsms_web import TsmsWeb

logging.basicConfig(level=logging.INFO, format='%(asctime)16s - %(levelname)8s - %(message)s')

'''前置'''
# @pytest_frame.fixture(scope='session')
# def login():
#     logging.info("执行登录")
#     tw = TsmsWeb()
#     tw.login('lijihua', 'lijihua198915')
#     assert tw.is_login('lijihua')

# @pytest_frame.fixture(scope="session")
# def login():
#     logging.info("session 前置")

# @pytest_frame.fixture(scope="module")
# def login():
#     logging.info("module 前置")

# @pytest_frame.fixture(scope="class")
# def login():
#     logging.info("class 前置")

# @pytest_frame.fixture(scope="function")
# def login():
#     logging.info("父级目录function 前置")


'''前置后置'''


'''强制后置'''
# @pytest_frame.fixture(scope="session")
# def login(request):
#     #后置，引用request的addfunalizer方法
#     def teardown_function1():
#         logging.info("强制后置1")
#     def teardown_function2():
#         logging.info("强制后置2")
#     request.addfinalizer(teardown_function2)
#     request.addfinalizer(teardown_function1)
#
#     #前置
#     logging.info("这是前置，尽管我被写在后面")

'''自动前置'''
#userfixtures装饰:@pytest_frame.mark.usefixtures("login") 。注意 "login" 是函数名的字符串值

# sco = "module"
# @pytest_frame.fixture(scope=sco,autouse=True)
# def login():
#     logging.info("父级目录自动生效{}前置".format(sco))
#     yield
#     logging.info("父级目录自动生效{}后置".format(sco))

#autouse自动生效
sco = "module"
# @pytest_frame.fixture(scope=sco,autouse=True)
# def login():
#     logging.info("父级目录自动生效{}前置".format(sco))
#     yield
#     logging.info("父级目录自动生效{}后置".format(sco))

'''***** fixture传值'''
# @pytest_frame.fixture(scope=sco)
# def login():
#     logging.info("自定义前置")
#     return 200

# def open(login):
#     l = login
#     logging.info("自定义前置-返回值为")


'''fixture接受传参'''
@pytest.fixture(scope="function")
def login():
    def __login(sign_id):
        s = sign_id
        logging.info("删除的sign_id 为：{}".format(s))
        return 200
    return __login