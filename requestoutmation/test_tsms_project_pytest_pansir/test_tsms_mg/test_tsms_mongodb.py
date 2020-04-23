


class TestMongodb(object):

    def test_mongo_001(self, tb):
        # 查询审批通过的sign_id
        tb.tsms_get('sign')
        # print(ts.json)
        sign_id = tb.get_field('id', audit_status='passed')
        # print(sign_id)
        # #查询审批通过的sign_id下的审批通过的temp_id
        tb.tsms_get('temp')
        temp_id = tb.get_field('id', audit_status='passed', sign_id=sign_id)
        # print(temp_id)
        # #调取随机生成手机号方法生成手机号码
        phone = tb.gen_phones(1)
        # print(phone)

        data9 = {
            "sign_id": sign_id,
            "temp_id": temp_id,
            "mobiles": phone
        }
        tb.req_post('message', data9)
