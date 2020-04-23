import pytest, logging
from pytest_commons.tsms_base import Tsmstest
from pytest_config.tsms_base_config import *

logging.basicConfig(level=logging.INFO, format='%(asctime)16s - %(levelname)8s - %(message)s')

# 申明夹具
ts = Tsmstest()
send_para_fail = ts.gen_para_fail('message')

# 异常场景
test_send_param_fail = [
    # 1. sign_id和temp_id不匹配
    {"sign_id": 1, "http_code": 403, "expect": {'error': 'ER:0023', 'message': 'sign id is not belong to user'}},
    # 2. temp_id审核未通过
    {"sign_id": data_config.get("default_sign_id"), "temp_id": data_config.get("not_pass_temp_id"), "http_code": 403, "expect": {'error': 'ER:0032', 'message': 'temp is not passed'}},
]


class TestSendMessage(object):
    @pytest.mark.level3
    @pytest.mark.parametrize("send_para_fail", test_send_param_fail, indirect=True)
    def test_send_message_api_001(self, send_para_fail):
        """
        测试一般异常场景，只校验接口返回
        """
        logging.info('[测试异常场景]')
