import random
from tenacity import retry, stop_after_attempt, wait_exponential

class TestTsmsKafkaAnalysis(object):

    def test_kafka_001(self, kfk, tm):
        """直接写数据到kafka，验证kafka"""
        #1、构造测试数据
        uid = random.randint(100000000, 999999999)
        phone = "13100368311"
        content = "【联通号码】好饿，好饿，好饿"
        data = {
            "uid": uid,
            "phone": phone,
            "content": content
        }
        #2、直接写数据到kafka
        kfk.send_data_secure(data)
        #3、查mongodb，并断言结果，错误重试
        # tm.mongo_tsms(uid=uid)
        self.check_mongodb(uid, tm)


    @retry(stop=stop_after_attempt(5), wait=wait_exponential(multiplier=2, max=5))
    def check_mongodb(self, uid, tm):
        """错误重试，查询mongodb"""
        res = tm.mongo_tsms(uid=uid)
        assert res.get('uid') == uid
        assert tm.res.get('sign') == '联通号码'
        assert tm.res.get('phone_type') == '联通'