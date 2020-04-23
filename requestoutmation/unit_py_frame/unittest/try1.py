from tsms.tsms_base import Tsmstest
import requests, unittest, re, logging

logging.basicConfig(level=logging.INFO, format=('%(asctime)-16s %(levelname)-8s %(message)s'))
ts = Tsmstest()
class Sign(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        '''获取登录session'''
        cls.s = requests.session()
        url = 'http://192.168.0.109:5001/login'
        data = {
            "username": "lijihua",
            "password": "lijihua198915",
        }
        # get请求login 获取csrf_token
        r = cls.s.get(url)
        # print(r)
        # 获取csrf_token
        csrf_token = re.findall(r'csrf_token.*?value="(.*?)">-', r.text)
        data["csrf_token"] = csrf_token
        #登录后获取cookies
        res = cls.s.post(url, data=data)
        logging.info('获取登录后的cookies为==：{}'.format(cls.s.cookies))
        assert res.status_code == 200
        assert 'Welcome' in res.text, '登录失败'
        print('-----ok-----')

    @classmethod
    def tearDownClass(cls):
        pass



    def test1(self):
        url2 = 'http://192.168.0.109:5001/user/lijihua'
        res = self.s.get(url2)
        logging.info("/user/lijihua接口返回的结果为：{}".format(res.text))
        assert res.status_code == 200
        assert "资料编辑" in res.text, "/user/lijihua接口请求失败"
        print('-----ok------')

if __name__=='__main__':
    unittest.main()