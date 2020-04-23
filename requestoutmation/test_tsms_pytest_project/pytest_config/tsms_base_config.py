#env: 0为开试环境，1为测试环境，2为生产环境
env = 2

#测试url
header_url = 'http://192.168.0.180:5001'
#测试环境账号密码
user = 'lijihua'
passwd = 'lijihua198915'

#线上url
pro_header_url = 'http://www.captaintests.club' #http://www.captaintests.club/
#线上环境账号密码
# pro_user = 'carl'
# pro_passwd = 'lijihua198915'
pro_user = 'dcs'
pro_passwd = '123'


#root账号
root_user = "root"
root_passwd = '123'


url_config = {
    "pro": "http://www.captaintests.club",
    "test": "http://192.168.0.182:5001",
    "dev": "http://127.0.0.1:5001",
    "default_headers": {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36",
        "Content-Type": "application/json"
    },
    "tieba": "https://tieba.baidu.com/hottopic/browse/topicList",

}

account_config = {
    "default_user": "dcs",
    "default_passwd": 123,
    "root_user": "root",
    "root_passwd": 123
}

data_config = {
    "default_heads": "130,131,132,145,146,155,156,166,167,1704,1707,1708,1709,171,175,176,185,186",
    "default_sign_id": 542,  # is pass
    "default_temp_id": 56,  # is pass
    "not_pass_sign_id": 161,
    "not_pass_temp_id": 57
}
