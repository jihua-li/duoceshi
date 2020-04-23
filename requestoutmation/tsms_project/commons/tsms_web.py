import logging,re,requests
import tsms_project.config.tsms_base_config as config
from tsms_project.commons.tsms_decorator import logit

logging.basicConfig(level=logging.INFO, format=('%(asctime)-16s %(levelname)-8s %(message)s'))

class TsmsWeb:
    def __init__(self, env = None):
        self.s = requests.session()
        if env:
            self.env = env
        else:
            self.env = config.env
        if self.env == 0:
            pass
        elif self.env == 1:
            self.header_url= config.header_url
            self.user = config.user
            self.passwd = config.passwd
        elif self.env == 3:
            self.header_url = config.pro_header_url
            self.user = config.pro_user
            self.passwd = config.pro_passwd
        else:
            self.header_url = config.header_url
            self.user = config.user
            self.passwd = config.passwd

    @logit
    def login(self, user, passwd):
        '''
        执行登录操作，包括获取登录是需要的token
        :param user: 登录用户名
        :param passwd: 登录密码
        :return: 将cookies写进self.s, 同时返回登录成功后的返回内容
        '''
        url = self.header_url + '/login'
        #获取token
        try:
            r = self.s.get(url)
            csrf_token = re.findall(r'csrf_token.*?value="(.*?)">-', r.text)[0]
            logging.info('[获取页面token]：{}'.format(csrf_token))
        except:
            logging.warn('[获取页面token失败]')
            return

        #3. 参数化要发送的数据
        data = {
            "username": self.user,
            "password": self.passwd,
            "submit": "Login",
            "csrf_token": csrf_token
        }
        #执行登录操作,获取登录token
        res = self.s.post(url, data)
        logging.info(res.status_code)
        return res.text

    @logit
    def is_login(self, user):
        '''
        判断是否登录成功
        :param user: 登录用户名
        :return: True /False
        '''
        url = self.header_url + '/user/{}'.format(self.user)
        logging.info(url)
        res = self.s.get(url)
        if "资料" in res.text:
            logging.info("登录成功")
            return True
        else:
            logging.info("登录失败")
            return False

    @logit
    def reg_sign(self, user):
        '''
        sign相关接口查询及前端数据提取
        :param user: 登录用户名
        :return: 正则提取后的list
        '''
        url = self.header_url + '/user/{}/sign'.format(self.user)
        html = self.s.get(url).text
        sign_list = re.findall("<tr>.*?<p>(.*?)</p>.*?<p>(.*?)</p>.*?<p>(.*?)</p>.*?<p>(.*?)</p>.*?</tr>", html, re.S)
        # logging.info(sign_list)
        return sign_list

    @logit
    def reg_temp(self, html):
        pass

    @logit
    def reg_send(self, user):
        """获取/user/user/history接口前端数据"""
        url = self.header_url + "/user/%s/history" % self.user
        logging.info("[现在要正则匹配的页面是]: {}".format(url))
        html = self.s.get(url).text
        a = re.findall("<tr>.*?<p>(.*?)</p>.*?<p>(.*?)</p>.*?<p>(.*?)</p>.*?<p>(.*?)</p>.*?<p>(.*?)</p>.*?</tr>", html, re.S)
        return a

    @logit
    def get_res(self, exp_id, records_list):
        """从列表中取指定的数据"""
        exp_res = ''
        for record in records_list:
            #注意传入的exp_id可能是int类型，这里需要强制转换成str类型
            if str(exp_id) in record:
                exp_res = record
        return exp_res



# if __name__ =='__main__':
    # user = 'carl'
    # passwd = 'lijihua198915'
    # tw = TsmsWeb()
    # tw.login(user, passwd)
    # a = tw.is_login(user)
    # assert a == True
    # rs = tw.reg_sign(user)
    # for r in rs:
    #     print(r[1],r[2],r[3])

