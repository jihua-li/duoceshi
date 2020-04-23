import pytest,logging

logging.basicConfig(level=logging.INFO, format='%(asctime)16s - %(levelname)8s - %(message)s')


# 定义命令 参数
# 1. 在  中，可直接通过 pytestconfig.getoption('--host') 获取
def pytest_addoption(parser):
    # 定义命令 参数
    parser.addoption('--host_addr', action='store', default=None, help='传host地址')
    parser.addoption('--startall', action='store', default=None, help='标示执全部  ')


# 2. 可通过 法返回，然后通过fixture透传，注意:这 使 pytestconfig获取参数
# @pytest.fixture()
# def host_address1(pytestconfig):
#     # 这 的host_add 定义命名，将整个结果返回
#     logging.info("[pytestconfig为]: {}".format(pytestconfig))
#     return pytestconfig.getoption('--host_addr')


@pytest.fixture()
def host_address2(request):
    # 这 的host_add 定义命名，将整个结果返回
    host_addr = request.config.getoption('--host_addr')
    logging.info(host_addr)
    return host_addr
