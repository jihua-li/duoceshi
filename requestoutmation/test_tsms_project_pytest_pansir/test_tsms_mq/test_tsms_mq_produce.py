import logging, json
from tsms_pytest_commons.tsms_db import TsmsDB
from tenacity import retry, stop_after_attempt, wait_random_exponential

logging.basicConfig(level=logging.INFO, format='%(asctime)-16s %(levelname)-8s %(message)s')

td = TsmsDB()


class TestTsmsMqProduce(object):
    uuid = "a1e2ff2e-23c5-11ea-a694-acde48001122"

    @retry(stop=stop_after_attempt(5), wait=wait_random_exponential(2, max=5))
    def db_retry(self, uuid):
        """
        异步数据校验，重试查询数据库
        """
        res = td.tsms_select("send", "consume,status,mobile", uuid=uuid)
        assert res["status"] == "success"

    def test_pro_01(self, mq, td):
        data = {
            "uid": self.uuid,
            "phone": "17134198056",
            "content": "【hellokitty】验证码为：123"
        }
        # 改为failed
        td.tsms_update("send", "status", "failed", uuid=self.uuid)
        res = td.tsms_select("send", "status", uuid=self.uuid)
        assert res.get("status") == "failed"
        # 写mq
        mq.push_direct_secure(json.dumps(data))
        # 再查数据库
        self.db_retry(self.uuid)
