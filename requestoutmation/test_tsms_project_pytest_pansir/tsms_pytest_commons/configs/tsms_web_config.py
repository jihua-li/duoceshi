url_web = "http://127.0.0.1:5001"
account_config = {
    "default_user": "dcs",
    "default_passwd": 123,
}
url_config = {
    "login": url_web + "/login",
    "sign": url_web + "/user/{}/sign".format(account_config.get("default_user"))
}
