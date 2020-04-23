import pytest, logging
from tsms_pytest_commons.tsms_base import TsmsBase
from tsms_pytest_commons.tsms_web import TsmsWeb
from tsms_pytest_commons.tsms_db import TsmsDB
from tsms_pytest_commons.tsms_rds import TsmsRedis
from tsms_pytest_commons.tsms_mq import MQPush

logger = logging.getLogger(__name__)


def pytest_addoption(parser):
    parser.addoption('--env', action='store', default=None, help='指定环境')


@pytest.fixture()
def login_1():
    """不需要和用例进行数据交互"""
    logging.info("测试流程")


@pytest.fixture()
def login_2():
    """需要得到前置，后置的返回数据"""
    logging.info("测试流程")
    return 200


@pytest.fixture()
def login():
    """这个已经不是不同意义上的前置"""
    """测试夹具"""

    def _login(sign_id):
        a = sign_id
        logging.info("删除sign id is {}".format(a))
        status = 200
        return status

    return _login


@pytest.fixture(scope="function")
def tb(pytestconfig):
    logging.info("[环境参数为]: {}".format(pytestconfig.getoption("--env")))
    if pytestconfig.getoption("--env") == "pro":
        return TsmsBase(env=2)
    else:
        return TsmsBase()


@pytest.fixture()
def td():
    return TsmsDB()


@pytest.fixture()
def tw():
    return TsmsWeb()


@pytest.fixture()
def rds():
    return TsmsRedis()


@pytest.fixture()
def mq():
    return MQPush()


@pytest.fixture(scope="session")
def web_session():
    return TsmsWeb().get_web_session()


@pytest.fixture(scope="session")
def clear_sign_all():
    """
    统计sign_id，最后统一清理
    """
    pytest.sign_ids = []
    yield
    sign_ids = pytest.sign_ids
    if not sign_ids:
        logger.info("[当前sign_id列表为]: {} 不需要清理".format(sign_ids))
        return
    logger.info("[经过一轮测试，新增的sign_id是]: {}".format(sign_ids))
    try:
        ts = TsmsBase()
        for sign_id in sign_ids:
            ts.req_delete("sign", {"sign_id": sign_id})
            if ts.status_code != 200:
                logger.warning("[签名删除失败，签名id为]：{}".format(sign_id))
    except Exception as e:
        logger.error(e)


@pytest.fixture(scope="function")
def clear_sign():
    """
    指定sign_id进行清理
    """

    def _clear_sign(sign_id):
        logger.info("[将要删除的sign_id是]: {}".format(sign_id))
        try:
            ts = TsmsBase()
            ts.req_delete("sign", {"sign_id": sign_id})
            if ts.status_code != 200:
                logger.warning("[签名删除失败，签名id为]：{}".format(sign_id))
            return ts.status_code
        except Exception as e:
            logger.error(e)

    return _clear_sign


@pytest.fixture()
def create_sign():
    """创建一个新签名"""
    tb = TsmsBase()
    data = tb.sign_data()
    tb.req_post("sign", data)
    # get取值，不会报错，取不到，返回None
    return tb.json.get("sign_id")
    # 取不到，抛出异常
    # return tb.json["sign_id"]


@pytest.fixture()
def rejected_sign():
    """创建一个新签名，并审核为rejected"""
    tb = TsmsBase()
    data = tb.sign_data()
    tb.req_post("sign", data)
    sign_id = tb.json.get("sign_id")
    tb.review("sign", sign_id, audit_status="rejected")
    return sign_id


@pytest.fixture(scope="function")
def sign_para_fail(request):
    """
    单个测试夹具：测试所有异常data
    """
    # 动态数据
    tb = TsmsBase()
    data = tb.sign_data()
    code = request.param.get("http_code")
    exp = request.param.get("expect")
    for k, v in request.param.items():
        if k in data:
            data[k] = v
    tb.req_post("sign", data=data)
    assert tb.status_code == code
    assert tb.json == exp
