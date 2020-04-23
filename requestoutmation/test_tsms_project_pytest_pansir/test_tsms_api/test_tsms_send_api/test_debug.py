import logging, pytest
import random, requests
from configs.tsms_base_config import *

logger = logging.getLogger(__name__)


def test_01(tb, clear_sign):
    # tb 就相当于 import 实例
    data = tb.sign_data()
    tb.req_post("sign", data)
    assert tb.status_code == 200
    # assert tb.json ==
    clear_sign(tb.json.get("sign_id"))


def test_fix(login, login2, create_sign):
    logging.info("用例本体")


def test_fix1(login):
    a = login(1)
    logging.info(a)
    logging.info(type(a))
    # logging.info("用例用例")


@pytest.mark.usefixtures("clear_sign_all")
def test_create1():
    logging.info("创建签名id")
    sign_id = 123
    # 收集id
    pytest.sign_ids.append(sign_id)


def test_create2(clear_sign_all):
    logging.info("创建签名id")
    sign_id = 124
    pytest.sign_ids.append(sign_id)


class Test111():
    # url = "http://127.0.0.1:5501/v1/signature"
    url = url_config.get("test") + url_config.get("api3")
    data = {
        "signature": "hello",
        "source": "string",
        "pics": []
    }

    def test_1(self, tb):
        # logger.info("okk")
        # logger.info(random_1(self.test_1))
        logger.info(tb.send_data(1))

    def test_2(self, tb):
        # logger.info("ok")
        # logger.info(random_1(self.test_1))
        logger.info(tb.send_data(2))


if __name__ == '__main__':
    pytest.main()
