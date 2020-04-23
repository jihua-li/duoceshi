import logging, os, random, string, requests, json
from robot_commons.tsms_decorator import use_logging, logit
from config import tsms_base_config


class Tsmstest(object):
    def __init__(self, env=0):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36",
            "Content-Type": "application/json"
        }
        self.tieba = 'https://tieba.baidu.com/hottopic/browse/topicList'
        self.default_phone_heads = '130,131,132,145,146,155,156,166,167,1704,1707,1708,1709,171,175,176,185,186'
        self.exp_str = ''
        # self.exp_list = []
        if env:
            self.env = env
        else:
            self.env = tsms_base_config.env
        if self.env == 0:
            pass
        elif self.env == 1:
            self.head_url = tsms_base_config.header_url
            self.user = tsms_base_config.user
            self.passwd = tsms_base_config.passwd
        elif self.env == 2:
            self.head_url = tsms_base_config.pro_header_url
            self.user = tsms_base_config.pro_user
            self.passwd = tsms_base_config.pro_passwd
        else:
            self.head_url = tsms_base_config.header_url
            self.user = tsms_base_config.user
            self.passwd = tsms_base_config.passwd
        # 初始化一个全局session对象
        # self.s = requests.session()
        self.status_code = ''
        self.text = ''
        self.json = {}
        self.root_user = tsms_base_config.root_user
        self.root_passwd = tsms_base_config.root_passwd
        self.t_id = ''

    def choie_url(self, url_type):
        if url_type == 'sign':
            url = self.head_url + '/v1/signature'
        elif url_type == 'temp':
            url = self.head_url + '/v1/template'
        elif url_type == 'message':
            url = self.head_url + '/v1/message'
        elif url_type == 'temp_review':
            url = self.head_url + '/v2/tempreview'
        elif url_type == 'charge':
            url = self.head_url + '/v2/charge'
        else:
            return url_type
        logging.info("[当前请求的地址是]: {}".format(url))
        return url
    @logit
    def req_get(self, url, *, headers=None):
        '''请求前端链接，获取到一个json数据 或 text数据'''
        if headers:
            hd = headers
        else:
            hd = self.headers
        r = requests.get(url, headers=hd)
        try:
            res = r.json()
        except Exception as e:
            res = r.text
        return res
    @logit
    def tsms_get(self, url_type, user=None, passwd=None, *, headers=None):
        url = self.choie_url(url_type)
        if headers:
            hd = headers
        else:
            hd = self.headers
        if user and passwd:
            user, passwd = user,passwd
        elif not user and not passwd:
            user,passwd= self.user,self.passwd
        elif not user:
            user, passwd= self.user, passwd
        elif not passwd:
            user, passwd= user, self.passwd
        else:
            user ,passwd = self.user, self.passwd
        logging.info("[传入的用户名，密码分别为]：{},{}".format(user, passwd))

        response = requests.get(url, auth=(user, passwd), headers=hd)
        self.status_code = response.status_code
        logging.info("[返回码是:] {}".format(self.status_code))
        self.json = response.json()
        logging.info("[返回内容是]: {}".format(self.json))
        return self.json

    @logit
    def req_post(self, url_type, data, user=None, passwd=None, *, headers=None):
        '''post请求方法封装'''
        url = self.choie_url(url_type)
        logging.info('[type(data)]:{}{}'.format(type(data),data))
        if isinstance(data, str):
            try:
                data = json.loads(data)
            except Exception as err:
                logging.error('[data参数传入数据类型错误，只能传json格式数据]')
                raise err
        else:
            data = data

        if headers:
            hd = headers
        else:
            hd = self.headers
        if user and passwd:
            user, passwd = user, passwd
        elif not user and not passwd:
            user,passwd= self.user, self.passwd
        elif not user:
            user, passwd= self.user, passwd
        elif not passwd:
            user, passwd= user, self.passwd
        else:
            user ,passwd = self.user, self.passwd
        logging.info("[传入的用户名，密码分别为]：{},{}".format(user, passwd))
        response = requests.post(url, json=data, auth=(user, passwd), headers=hd)

        self.status_code = response.status_code
        logging.info("[返回码是]： {}".format(self.status_code))
        try:
            self.json = response.json()
            logging.info("[返回内容是]: {}".format(self.json))
            for key, value in self.json.items():
                if 'id' in key:
                    self.t_id = value
            return self.json

        except:
            self.text = response.text
            logging.info("[返回的内容是]：{}".format(self.text))
            return self.text

    @logit
    def req_put(self, url_type, data, user, passwd, *, headers=None):
        '''put请求方法封装'''
        url = self.choie_url(url_type)
        if headers:
            hd = headers
        else:
            hd = self.headers
        if user and passwd:
            user, passwd = user,passwd
        elif not user and not passwd:
            user,passwd= self.user,self.passwd
        elif not user:
            user, passwd= self.user, passwd
        elif not passwd:
            user, passwd= user, self.passwd
        else:
            user ,passwd = self.user, self.passwd

        logging.info("[传入的用户名，密码分别为]：{},{}".format(user, passwd))
        response = requests.put(url, json=data, auth=(user, passwd), headers=hd)  # 修改审核结果需要root账号
        self.status_code = response.status_code
        logging.info("[返回码是]： {}".format(self.status_code))
        self.json = response.json()
        logging.info("[返回内容是]: {}".format(self.json))
        return self.json

    @logit
    def req_del(self, url_type, data, user, passwd, *, headers=None):
        '''del请求方法封装'''
        url = self.choie_url(url_type)
        if headers:
            hd = headers
        else:
            hd = self.headers
        if user and passwd:
            response = requests.delete(url, json=data, auth=(user, passwd), headers=hd)
        elif not user and passwd:
            response = requests.delete(url, json=data, auth=(self.user, passwd), headers=hd)
        elif user and not passwd:
            response = requests.delete(url, json=data, auth=(user, self.passwd), headers=hd)
        else:
            response = requests.delete(url, json=data, auth=(self.user, self.passwd), headers=hd)
        self.status_code = response.status_code
        logging.info("[返回码是：{}]".format(self.status_code))
        # if self.status_code == 200:
        #     self.text = response.text
        #     logging.info("[返回内容是]：{}".format(self.text))
        #     return self.text
        # else:
        #     self.json = response.json()
        #     logging.info("[返回内容是]：{}".format(self.json))
        #     return self.json
        try:
            self.json = response.json()
            logging.info("[返回的内容是]：{}".format(self.json))
            return self.json
        except Exception as err:
            logging.info(err)
            self.text = response.text
            logging.info("[返回的内容是]：{}".format(self.text))
            return self.text

    def recur(self, key, res):
        '''从字典中解析需要的字段，将所有解析结果组成列表返回'''
        self.exp_list = []

        def get(getkey, res_dict):
            if isinstance(res_dict, dict):
                for key, value in res_dict.items():
                    if key == getkey:
                        logging.info("[当前解析的字段是 {} 解析结果是]: {}".format(key, value))
                        self.exp_list.append(value)
                        break
                    get(getkey, value)
            elif isinstance(res_dict, list):
                for ele in res_dict:
                    get(getkey, ele)

        get(key, res)
        if len(self.exp_list) == 1:
            return self.exp_list[0]
        return self.exp_list

    def download_by_url(self, url, dir='testdata'):
        '''通过链接下载内容，存放到本地'''
        pic_path = os.path.join(os.getcwd(), dir)
        name = ''.join(random.sample(string.ascii_lowercase, 5)) + '.jpg'
        pic_name = os.path.join(pic_path, name)
        with open(pic_name, 'wb') as f:
            r_pic = requests.get(url, headers=self.headers)
            f.write(r_pic.content)
            f.close()

    def download_all(self, url_list):
        '''下载所有链接'''
        if isinstance(url_list, list):
            for url in url_list:
                logging.info("[当前下载的链接是]: ".format(url))
                self.download_by_url(url)
        else:
            logging.error("[传入的链接格式有误]:".format(url_list))

    @logit
    def gen_ranstr(self, num_int=0, num_letters=0, num_zh=0, num_pun=0):
        '''生成随机字符串'''
        a = [random.choice(string.digits) for i in range(int(num_int))]
        b = [random.choice(string.ascii_letters) for i in range(int(num_letters))]
        c = [chr(random.randint(0x4e00, 0x9fbf)) for i in range(int(num_zh))]
        d = [random.choice(string.punctuation) for i in range(int(num_pun))]
        ran_list = a + b + c + d
        random.shuffle(ran_list)
        return ''.join(ran_list)

    @use_logging
    def gen_phones(self, num, phone_heads=None):
        '''生成随机号码，可以指定数量，返回一个列表'''
        if not phone_heads:
            phone_heads = self.default_phone_heads
        head_list = phone_heads.split(',')
        phone_list = []
        for i in range(int(num)):
            phone_head_list = random.sample(head_list, 1)
            phone_head = phone_head_list[0]
            len_body = 11 - len(phone_head)
            b = ''.join(random.sample(string.digits, len_body))
            phone = phone_head + b
            phone_list.append(phone)
        return phone_list

    def check_sign(self):
        assert isinstance(self.json["sign_id"], int), "签名id类型有误"

    def get_exp(self, getkey, resdict):
        '''递归函数，下载图图片，随机函数'''
        exp = []

        def get_value(get_key, res_dict):
            if isinstance(res_dict, dict):
                for k, v in res_dict.items():
                    if k == get_key:
                        # 把数据增加到exp中
                        exp.append(v)
                    get_value(get_key, v)
            elif isinstance(res_dict, list):
                for ele in res_dict:
                    get_value(get_key, ele)

        get_value(getkey, resdict)
        return exp

    def signid_exist(self, sign_id):
        '''封装判断签名ID是否存在'''
        # 查询签名id
        res = self.tsms_get('sign')
        # 调用递归方法，对签名id进行递归查询
        exp = self.get_exp('id', res)
        if sign_id in exp:
            return True
        else:
            return False

    @logit
    def req_audit(self, audit_type, reviwe_id, audit_status, reject_reason=None, user=None, passwd=None):
        '''审核功能接口，兼容签名和模版审核'''
        data = {
            "audit_status": audit_status,
            "reject_reason": reject_reason,
        }
        if audit_type == "sign":
            url = self.head_url + "/v2/signreview"
            data["sign_id"] = reviwe_id
        elif audit_type == "temp":
            url = self.head_url + "/v2/tempreview"
            data["temp_id"] = reviwe_id
        else:
            logging.error("[审核参数有误]：".format(audit_type))
            return
        logging.info("[请求的接口地址是]：{}".format(url))
        res = requests.post(url, json=data, auth=(self.root_user, self.root_passwd), headers=self.headers)
        self.status_code = res.status_code
        try:
            self.json = res.json()
            logging.info("[返回的内容是]：{}".format(self.json))
            logging.info("[审核结果是]：{}/{}".format(self.status_code, self.json))
            return self.json
        except Exception as err:
            self.text = res.text
            logging.info("[返回的内容是]：{}".format(self.text))
            logging.info("[审核结果是]：{}/{}".format(self.status_code, self.text))
            return self.text

    @logit
    def get_field(self, feild, **kwargs):
        """解析get请求的指定字段"""
        for k, v in kwargs.items():
            for d in self.json['items']:
                if d[k] == v:
                    return d[feild]
        logging.error("[未找到指定字段]:{}".format(feild))

    @logit
    def get_tsms_uuid(self):
        '''获取uuid'''
        return self.json['uuid']

    @logit
    def get_t_id(self):
        return self.t_id

    @logit
    def check_tsms_uuid(self):
        assert isinstance(self.json['uuid'], str)

    @logit
    def check_status_code(self, code):
        assert self.status_code == int(code)



if __name__ == '__main__':
    ts = Tsmstest()
    # a = ts.gen_phones(10, "139,189")
    # print(a)
    # b = ts.gen_ranstr(2, 2, 2, 2)
    # print(b)
    # s = ts.signid_exist(101)
    # print(s)

