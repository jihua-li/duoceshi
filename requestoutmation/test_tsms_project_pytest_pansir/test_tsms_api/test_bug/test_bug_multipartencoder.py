import logging, requests, pytest
from requests_toolbelt import MultipartEncoder

logger = logging.getLogger()


class TestBugMultiPartEncoder(object):
    @pytest.mark.skip("debug")
    def test_01(self):
        """写死的，相同的数据，可以连续请求两次"""
        url = "http://httpbin.org/post"
        data = {"name": "hello"}
        r = requests.post(url, data=data)
        logging.info("{} {}".format(r.status_code, r.text))
        r = requests.post(url, data=data)
        logging.info("{} {}".format(r.status_code, r.text))

    @pytest.mark.skip("debug")
    def test_02(self):
        """找到原因，MultipartEncoder 数据不能连续请求"""
        url = "http://httpbin.org/post"
        data = MultipartEncoder(
            fields={
                'signId': "123",
                'tempId': "123",
                'schedule': "false",
                'tag': '',
            }
        )
        r = requests.post(url, data=data)
        logging.info("{} {}".format(r.status_code, r.text))
        r = requests.post(url, data=data)
        logging.info("{} {}".format(r.status_code, r.text))

    @pytest.mark.skip("debug")
    def test_03(self):
        """使用原生的方法传参，可以连续两次"""
        url = "http://httpbin.org/post"
        data = {
            "sign": (None, "123"),
            "tempId": (None, "123"),
        }
        r = requests.post(url, data=data)
        logging.info("{} {}".format(r.status_code, r.text))
        r = requests.post(url, data=data)
        logging.info("{} {}".format(r.status_code, r.text))
