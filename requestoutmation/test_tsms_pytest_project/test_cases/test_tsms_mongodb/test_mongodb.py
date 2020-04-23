import time, logging
from tenacity import retry, stop_after_attempt, wait_exponential

logging.basicConfig(level=logging.INFO, format='%(asctime)-16s %(levelname)-8s %(message)s')


class TestMongodb(object):




    def test_mongo_001(self, ts, tm):
        # 查询审批通过的sign_id
        ts.tsms_get('sign')
        # print(ts.json)
        sign_id = ts.get_field('id', audit_status='passed')
        # print(sign_id)
        # #查询审批通过的sign_id下的审批通过的temp_id
        ts.tsms_get('temp')
        temp_id = ts.get_field('id', audit_status='passed', sign_id=sign_id)
        # print(temp_id)
        # #调取随机生成手机号方法生成手机号码
        phone = ts.gen_phones(1)
        # print(phone)

        data9 = {
            "sign_id": sign_id,
            "temp_id": temp_id,
            "mobiles": phone
        }
        ts.req_post('message', data9)
        uuid = ts.json['uuid']

        # time.sleep(2)
        #查mongodb数据
        # tm.mongo_tsms(uid=uuid)
        self.check_mongodb(uuid, tm)

    @retry(stop=stop_after_attempt(5), wait=wait_exponential(multiplier=2, max=5))
    def check_mongodb(self, uuid, tm):
        res = tm.mongo_tsms(uid=uuid)
        assert res.get('uid') == uuid