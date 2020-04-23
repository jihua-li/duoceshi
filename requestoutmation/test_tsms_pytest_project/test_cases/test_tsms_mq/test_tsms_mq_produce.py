import pytest, logging, json
from tenacity import retry, stop_after_attempt, wait_random_exponential

class TestJJ():
    def test_01(self):
        pass

class TestPushMq(object):
    """mq测试用例"""
    uuid = '367dab7a-2a1a-11ea-90ca-acde48001122'

    @retry(stop=stop_after_attempt(5), wait=wait_random_exponential(2, max=5))
    def db_retry(self, uuid, od):
        """异步数据校验，重试查询数据库"""
        res = od.tsms_select('sms_send', 'consume,status,mobile', uuid)
        assert res[0].get("status") == "success"



    def test_push_001(self, mq, od):
        """消息发送MQ生产消费功能测试"""

        data = {
            "uid": self.uuid,
            "phone": "18535941072",
            "content": "【hellokitty】验证码为:1234"
        }

        #将测试数据状态改为failed
        od.tsms_update('sms_send', 'status', 'failed', uuid=self.uuid)
        res = od.tsms_select('sms_send', 'status', uuid=self.uuid)
        assert res[0].get("status") == "failed"

        #写MQ,将字典data通过json序列化成json字符串
        mq.push_direct_secure(json.dumps(data))

        #查数据库
        self.db_retry(self.uuid)

