import logging,pytest,time

logging.basicConfig(level=logging.INFO, format='%(asctime)s-%(levelname)s-%(message)s')

#方法一，一个一个清
# class TestDeleteSign(object):
#     '''删除sign id api测试'''
#     def test_case_01(self, delete_sign):
#         res = delete_sign(123)
#         assert res == 200

#方法二：执行所有用例后一起清
# @pytest.mark.usefixtures("delete_sign_all")
class TestDeleteSign(object):
    '''删除sign_id测试'''
    # def test_case_01(self, ts):
    #     data = ts.sign_data()
    #     ts.req_post('sign', data)
    #     pytest.sign_ids.append(ts.json['sign_id'])
    #
    # def test_case_02(self, ts):
    #     data = ts.sign_data()
    #     ts.req_post('sign', data)
    #     pytest.sign_ids.append(ts.json['sign_id'])

    @pytest.mark.timeout(2) #用例超时
    # @pytest.mark.flaky(reruns=5, reruns_delay=1) #用例重试
    def test_case_03(self):
        time.sleep(1)
        logging.info('start run test_case_03')
        pytest.assume(1 + 2 == 3) #多重校验，抛出所有断言失败的结果
        pytest.assume(1 + 2 == 3)
        pytest.assume(1 + 3 == 4)
