import logging, pytest
from pytest_commons.tsms_base import Tsmstest
from pytest_commons.tsms_web import TsmsWeb
from pytest_commons.tsms_mq import MQPush
from pytest_commons.tsms_db import OperationDb
from pytest_commons.tsms_redis import TsmsRedis
from pytest_commons.tsms_mongo import TsmsMongo
from pytest_commons.tsms_kafka import KafkaSender
from pytest_commons.tsms_decorator import use_logging, logit

logging.basicConfig(level=logging.INFO, format='%(acstime)s-%(levelname)s-%(message)s')

def pytest_addoption(parser):
    """定义命令行参数"""
    parser.addoption('--env', action='store', default=None, help='传入环境选择参数')

@pytest.fixture(scope='function')
def env_choice(pytestconfig):
    """用例执行环境选择夹具"""
    env = pytestconfig.getoption('--env')
    logging.info('env={}'.format(env))
    return env

@pytest.fixture(scope="function")
# @logit
def ts(pytestconfig):
    """Tsmstest类测试夹具"""
    env_type = pytestconfig.getoption('--env')
    logging.info('env_type: {}'.format(env_type))
    if env_type == 'test':
        return Tsmstest(env=1)
    elif env_type == 'pro':
        return Tsmstest(env=2)
    else:
        return Tsmstest(env=0)

# @pytest.fixture(scope='function')
# def ts():
#     """Tsmstest类测试夹具,pycharm运行代码时调用"""
#     return Tsmstest()

@pytest.fixture(scope="function")
def mq():
    """roabbitMQ测试类MQPush"""
    return MQPush()

@pytest.fixture(scope="function")
def tw():
    """TsmsWeb类测试夹具"""
    return TsmsWeb()

@pytest.fixture(scope="function")
def od():
    """数据库OperationDb类测试夹具"""
    return OperationDb()

@pytest.fixture(scope="function")
def tr():
    """redis TsmsRedis类测试夹具"""
    return TsmsRedis()

@pytest.fixture(scope='function')
def tm():
    """mongo TsmsMongo类测试夹具"""
    return TsmsMongo()

@pytest.fixture(scope='function')
def kfk():
    """kafka KafkaProducer类测试夹具"""
    return KafkaSender()

@pytest.fixture(scope="function")
def delete_sign():
    """删除sign_id"""
    def _delete_sign(sign_id):
        try:
            ts = Tsmstest()
            ts.req_del('sign', {"sign_id": sign_id})
            if ts.status_code != 200:
                logging.warning("[删除签名失败，签名id为]:{}".format(ts.status_code))
            return ts.status_code
        except Exception as err:
            logging.error(err)

    return _delete_sign


@pytest.fixture(scope="function")
def delete_sign_all(ts):
    """删除所有sign id"""
    pytest.sign_ids = []
    yield
    sign_ids = pytest.sign_ids
    if not sign_ids:
        logging.info("[当前sign_id列表为{}不需要删除]".format(sign_ids))
    logging.info("[经过一轮测试之后，新增的sign_id为]：{}".format(sign_ids))
    try:
        # ts = Tsmstest()
        for sign_id in sign_ids:
            ts.req_del('sign', {"sign_id": sign_id})
            if ts.status_code != 200:
                logging.warning("签名删除失败，sign_id为：{}".format(sign_id))
    except Exception as err:
        logging.error(err)


