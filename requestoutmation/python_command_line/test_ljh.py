'''
优势：
安装：
Pytest:

fixture自定义后置
'''
import logging, pytest, json, random
from json import JSONDecodeError
from pytest_frame.limits import limit_ver
logging.basicConfig(level=logging.INFO, format='%(asctime)16s - %(levelname)8s - %(message)s')


# @pytest_frame.fixture(scope="function") #标记为测试夹具
# def login():
#     logging.info("自定义前置")
#
# def test_hh(login):
#     logging.info("hehe")
#
# class Testhelo(object):
#     def test_01(self, login):
#         logging.info('执行第一条用例')
#         assert 2 == 1 + 1
#
#     def test_02(self, login):
#         logging.info('执行第二条用例')
#         assert 3 == 2 + 1



'''标记失败'''
#通过 marks=pytest_frame.mark.xfail 标记失败，则该场景不运行
# a = 'test_input,expected'
# b = [
#     ("1+2", 3),
#     ("2*3", 6),
#     pytest_frame.param("3-0", 3, marks=pytest_frame.mark.xfail),
# ]
#
# @pytest_frame.mark.parametrize(a, b)
# def test_eval(test_input, expected):
#     logging.info("执行测试用例")
#     assert eval(test_input) == expected
#     logging.info(test_input)
#     logging.info(expected)


#参数组合，利用嵌套装饰来可以实现参数组合
#应用场景，如入参组合传入校验
# @pytest_frame.mark.parametrize('a', [1, 2])
# @pytest_frame.mark.parametrize('b', [1, 3])
# def test_001(a, b):
#     logging.info('执行测试用例{} {}'.format(a, b))
#     assert a == b


#多重前置

#多重前置+多重param
# test_user = ["admin", "root"]
# test_pwd = ["123", 456]
#
# @pytest_frame.fixture(scope="module")
# def input_user(request):
#     user = request.param
#     # logging.info(user)
#     return user
#
# @pytest_frame.fixture(scope="module")
# def input_pwd(request):
#     pwd = request.param
#     # logging.info(pwd)
#     return pwd
#
# @pytest_frame.mark.parametrize("input_user", test_user, indirect=True)
# @pytest_frame.mark.parametrize("input_pwd", test_pwd, indirect=True)
# def test_login(input_user, input_pwd):
#     # logging.info("执行test_login测试用例")
#     a = input_user
#     b = input_pwd
#     logging.info("获取的数据组合为{} {}".format(a, b))


'''断言与异常'''
#常规写法
# def test_json_error1():
#     a = '''{'name':'dcs'}'''
#     try:
#         json.loads(a)
#     except JSONDecodeError as e:
#         # logging.info(e)
#         assert 'Expecting property name enclosed in double quotes: line 1 column 2 (char 1)' in str(e)

#pytest写法
# def test_login_error2():
#     b = '''{'name':'dcs'}'''
#     with pytest_frame.raises(JSONDecodeError) as e:
#         json.loads(b)
#     #断言异常类型type,从json中导入
#     logging.info(type(e.value))
#     assert e.type == JSONDecodeError
#     #断言异常value
#     assert 'Expecting property name enclosed in double quotes: line 1 column 2 (char 1)' in str(e.value)



'''用例跳过'''
#skip标记 @pytest_frame.mark.skip(reason="调试动作")
#直接跳过
#装饰器标记
# @pytest_frame.mark.skip(reason="调试动作，用例跳过")
# def test_skip1():
#     assert 1 == 2
#
# def test_skip2():
#     assert 1 == 1

#条件触发跳过
#当满足某个条件后，用例跳过
# def valid_config():
#     logging.info("判断配置是否正确")
#     return True
#
# def test_skip3():
#     if not valid_config():
#         pytest_frame.skip("配置错误")
#     logging.info("若果没有跳过，会执行这条")
#     assert 1 == 2
#
# def test_skip4():
#     assert 1 == 1

#skipif条件跳过
# @limit_ver
# def test_skip5():
#     assert 1 == 2
#
# def test_skip6():
#     assert 1 == 1

#xfail跳过
# login_data =[
#     {"user":"admin","pwd":"123"},
#     {"user":"root","pwd":"1234"}
# ]
# @pytest.fixture(scope="module")
# def login(request):
#     logging.info(request.param)
#     user = request.param["user"]
#     pwd = request.param["pwd"]
#     logging.info(user)
#     logging.info(pwd)
#     res = random.choice([True, False])
#     logging.info("登录状态是：{}".format(res))
#     return res
#
# @pytest.mark.parametrize("login", login_data, indirect=True)
# class TestMark(object):
#     @pytest.mark.level1
#     def test_login1(self, login):
#         res = login
#         if not res:
#             pytest.xfail("登录失败，标记为xfail")
#         logging.info("test_login1 ok")
#
#     @pytest.mark.level2
#     def test_login2(self, login):
#         logging.info("test_login2 ok")
#
#     @pytest.mark.level3
#     def test_login3(self, login):
#         logging.info("test_login3 ok")


'''用例标记'''
#命令行执行用例(选择多个标记执行用or) -->
# pytest /Users/lijihua/PycharmProjects/duoceshi/requestoutmation/unit_py_frame/pytest_frame/test_ljh.py -m "level1 or level2"

#定义一个标记为level1的测试用例：@pytest_frame.mark.level1

'''pytest自定义命令行'''
# def pytest_addoption(parser):
      #定义命令行参数
#     parser.addoption('--host_addr', action='store', default=None, help='传入host地址')
#     parser.addoption('--startall', action='store', default=None, help='表示执行全部用例')
#
# @pytest.fixture(scope='function')
# def host_address(pytestconfig):
#     logging.info("[pytestconfig为]：{}".format(pytestconfig))
#     return pytestconfig.getoption('--host_addr')




# def test_host_add1(host_address2):
#     ha = host_address2
#     logging.info(ha)

#
def test_host_add2(pytestconfig):
    logging.info(pytestconfig.getopiton('--host_addr'))

# def test_cmd_2(host_address2):
#     """通过夹具拿到外部变 """
#     logging.info(host_address2)
#     if host_address2:
#         host = host_address2
#     else:
#         host = '1.1.1.1'
#     logging.info("使用的host是:{}".format(host))
