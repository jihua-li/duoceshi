import pika, logging, json
from tenacity import retry, stop_after_attempt, wait_random_exponential
from test_tsms_pytest_project.pytest_commons.tsms_redis import TsmsRedis

logging.basicConfig(level=logging.INFO, format='%(asctime)-16s %(levelname)-8s %(message)s')
# tr = TsmsRedis()

def test_01():
    pass

class TestTsmsMqConsume(object):
    """mq对接生产者功能测试用例"""

    @retry(stop=stop_after_attempt(5), wait=wait_random_exponential(2, max=5)) #错误重试
    def rds_retry(self, uuid, exp, tr):
        #获取存入redis的值
        res = tr.get_redis_value('mq:{}'.format(uuid))
        assert json.loads(res) == exp

    def test_consume_001(self, ts, tr):
        """验证mq消费到的信息是否符合预期"""
        #获取请求数据
        data = ts.send_data()
        #发送消息
        ts.req_post('message', data)
        # 检查redis数据(消费到的真实数据)
        exp = {
            "uid": ts.json.get("uuid"),
            "phone": data.get("mobiles")[0],
            "content": "【passed】模版内容"
        }
        #调用查询redis方法，并进行错误重试
        self.rds_retry(ts.json.get('uuid'), exp, tr)


