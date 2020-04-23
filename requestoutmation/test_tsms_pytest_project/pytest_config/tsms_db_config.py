'''数据库相关配置'''
#env: 0为开试环境，1为测试环境，2为生产环境
env = 1

'''tsms测试环境'''
test_db_config = {
    'host':'192.168.0.101',#192.168.0.176  192.168.0.148
    'port':3306,
    'user':'root',
    'password':'123456',
    'db':'flaskblog',
    'charset':'utf8mb4'
}

'''tsms生产环境'''
pro_db_config = {
    'host':'148.70.194.135',
    'port':3306,
    'user':'debian-sys-maint',
    'password':'123456',
    'db':'flaskblog',
    'charset':'6udZCFBibeLtPuiG'
}

limit_fileds = ["audit_status","is_delete"]
