import logging, pytest
from tsms_pytest_commons.tsms_base import TsmsBase

logging.basicConfig(level=logging.INFO, format='%(asctime)-16s %(levelname)-8s %(message)s')


@pytest.fixture()
def tb_api():
    return TsmsBase()
