#env: 0为开试环境，1为测试环境，2为生产环境
env = 2

url_config = {
    "pro": "http://www.captaintests.club",
    "test": "http://127.0.0.1:5001",
    "dev": "http://127.0.0.1:5001",
    "default_headers": {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36",
        "Content-Type": "application/json"
    },
    "tieba": "https://tieba.baidu.com/hottopic/browse/topicList",
    "sign": "/v1/signature",
    "temp": "/v1/template",
    "message": "/v1/message",
    "send": "/v1/message",
    "sign_review": "/v2/signreview",
    "temp_review": "/v2/tempreview",
    "charge": "/v2/charge",
    "api3": "/v1/api3",
}

account_config = {
    "default_user": "dcs",
    "default_passwd": 123,
    "root_user": "root",
    "root_passwd": 123
}

data_config = {
    "default_heads": "130,131,132,145,146,155,156,166,167,1704,1707,1708,1709,171,175,176,185,186",
    "default_sign_id": 424,  # is pass
    "default_temp_id": 26,  # is pass
    "not_pass_sign_id": 436,
    "not_pass_temp_id": 27,
    "source_list": ["深圳", "广州"],
    "ljh_files": ["fie1", "fie2", "fie3",]
}
