import pytest, logging
from pytest_commons.tsms_base import Tsmstest


class TestSignApiCreate(object):
    """创建签名接口测试用例"""

    @pytest.mark.level1
    def test_sign_create_001(self, ts):
        """创建签名成功"""
        data = ts.sign_data()
        ts.req_post('sign', data=data)
        assert ts.status_code == 200

    @pytest.mark.level2
    def test_sign_create_002(self, ts):
        """创建签名失败"""
        logging.info('执行创建签名失败用例')
