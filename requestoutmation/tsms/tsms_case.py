from tsms.tsms_base import Tsmstest
import json, unittest


'''域名/接口地址：http://www.captaintests.club
@大家，接口测试服务我已经部署在了外网，大家可以测试一下看看可不可以使用。关于接口测试的练习大家可以在家里自行练习一下，注意几个点：
1. 我没有迁移数据，用户需要重新注册
2. 用的docker容器部署，数据不会落地
3. 测试发现500时，或者返回为html内容时，说明接口有误，不要重复请求了，有可能把服务弄挂，换一个场景进行测试，最好能把问题记一下发给我，我找时间修复
4. 大家先完成 第一组接口测试--签名相关的5个接口的测试，每个接口至少完成一个正常场景，一个异常场景'''


ts = Tsmstest()
signature = ts.gen_ranstr(num_letters=5)
print(signature)
data1 =  {
    "signature": signature,
    "source": "shenzhen",
    "pics": ["cc"]
    }
'''创建签名接口正常用例'''
# ts.req_post('sign',data1)
# print(ts.json)
# print(ts.status_code)
# assert ts.status_code == 200, '接口验证失败'
# assert isinstance(ts.json['sign_id'], int), '签名id类型有误'


'''创建签名接口异常用例，登录密码错误'''
# ts.req_post('sign',data1, user='lijihua', passwd='lijihua198916')
# assert ts.status_code == 400, '接口验证失败'
# assert ts.json['message'] == 'auth not pass', '接口返回参数异常'

'''查询签名接口正常用例'''
data2 = {}
# ts.tsms_get('sign')
# print(ts.json)

# assert ts.status_code == 200, '接口验证失败'


'''删除签名'''
#正常用例
# ts.req_post('sign',data1) #先创建一个账号
# sign_id = ts.json["sign_id"] #获取创建成功后的sign_id作为删除签名接口的入参
#
# data3 = {
# "sign_id": sign_id
# }
# ts.req_del('sign',data3) #删除签名
# assert ts.status_code == 200, "删除签名接口请求失败"
# assert ts.text == 'ok', "删除签名接口返回内容错误"
# assert False == ts.signid_exist(sign_id), "签名删除未成功，sign_id仍然存在"

#异常用例
data4 = {
"sign_id": 101
}
# ts.req_del('sign',data3) #删除签名
# assert ts.status_code == 403, "删除签名接口请求失败"
# assert ts.json == {'error': 'ER:0012', 'message': 'delete sign fail'}

#编写一个  ，创建一个签名，审核为不通过，然后再修改该签名，最后查看修改的字段是否准确
#创建一个签名
# ts.req_post('sign', data1)
# res1 = ts.json['sign_id']
# # print(res1)
#将创建的签名审核为不通过
ts.req_audit('sign', 542, 'passed', '审核通过')
print(ts.text)
# #修改签名为通过
# mod_sign = ts.gen_ranstr(3,3)
# data5 = {
#     "sign_id": res1, # 必填
#     "signature": mod_sign, # 必填
#     "source": 'hehe', # 必填
#     "pics": ['ddd'] # 选填
# }
# ts.req_put('sign', data5)
# assert ts.status_code == 200, "修改签名失败"
# assert ts.json['sign_id'] == res1, "修改后返回的sign_id与创建的sign_id不一致"
# #查询修改的签名字段
# ts.tsms_get('sign')

#审批签名
# sign_id = 113
# ts.req_audit('sign', sign_id, 'passed')
# assert ts.status_code == 200

'''temp接口测试用例'''
#创建模版
module = ts.gen_ranstr(3,3)
sign_id = "id"
data6 = {
    "name": module,
    "template": '模版内容',
    "type": 1,
    "description": '我要申请模版',
}
ts.req_post('temp', data6)
assert ts.status_code == 200
assert isinstance(ts.json['temp_id'], int), "创建模版失败"
#
# #查询模版
# temp_id = ts.json['temp_id'] #获取创建接口的temp_id
# ts.tsms_get('temp')
# name = ts.get_field('name', id = temp_id)
# # print(name)
# assert ts.status_code == 200
# assert module == name, "查询模版接口请求失败"
#
# #审核模版
# temp_id = 18
# ts.req_audit('temp', temp_id, 'passed') #rejected
# assert ts.status_code == 200
# assert ts.text == 'ok', "审核接口请求失败"
#
# #编辑模版
# data7 = {
#     "name": name,
#     "template": '修改后的模版内容',
#     "type": 1,
#     "description": '我要修改模版',
#     "sign_id": sign_id,
#     "temp_id": temp_id
# }
#
# ts.req_put('temp', data7)
# # assert ts.status_code == 200
# assert ts.json['temp_id'] == temp_id, "编辑模版接口返回值异常"
#
# #删除模版
# data8 = {
#     "sign_id": sign_id,
#     "temp_id": temp_id
# }
# ts.req_del('temp', data8)
# assert ts.status_code == 200
# assert ts.text == 'ok', "删除模版失败"

#短信发送
#查询审批通过的sign_id
ts.tsms_get('sign')
sign_id = ts.get_field('id', audit_status = 'passed')
print(sign_id)
#查询审批通过的sign_id下的审批通过的temp_id
ts.tsms_get('temp')
temp_id = ts.get_field('id', audit_status = 'passed',sign_id=sign_id)
print('temp_id为：{}'.format(temp_id))
#调取随机生成手机好方法生成手机好吗
phone = ts.gen_phones(1)
p =phone[0]
# print(phone)

data9 = {
    "sign_id": sign_id,
    "temp_id": temp_id,
    "mobiles": p
    }
ts.req_post('message', data9)
assert ts.status_code == 200
assert isinstance(ts.json['uuid'], str), "短信发送接口请求失败"