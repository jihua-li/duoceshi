#重点：缓存的方式
#懒汉式
#饥饿式
#定时周期

'''
远程访问redis -- ssh dcs@192.168.0.148 -p 1234
建立连接 -- redis-cli
鉴权 -- auth 123456（redis登录密码）

'''

#分布式锁
import redis,time

#创建redis连接池
# pool = redis.ConnectionPool(host ='192.168.0.148',port= 6379,password= '123456',db= 0,decode_responses= True)
# res = redis.Redis(connection_pool=pool)

#创建key,value
# res.set("lijihua","man")
# get_key = res.get("lijihua")
# print(get_key,type(get_key))
# assert res.exists("lijihua") == 1
#设置有效时间
# res.expire("lijihua", 5)
# time.sleep(5)
# #断言过期时间过期（-2）
# assert res.ttl("lijihua") == -2
# #断言key过期后是否被删除，0表示被删除，1表示存在
# assert res.exists('lijihua') == 0



'''把students表的数据导出来，全部刷到redis里面取'''
import records, redis
from tsms_project.commons.tsms_db import OperationDb

od = OperationDb()
#创建数据库连接
db = records.Database('mysql+pymysql://root:123456@192.168.0.148:3306/flaskblog?charset=utf8')
res = od.tsms_select("students", "*")
pool = redis.ConnectionPool(host='192.168.0.148', port=6379, password='123456', db=0, decode_responses=True)
r_bd = redis.Redis(connection_pool=pool)
# print(type(r))
#构造唯一key
dict_redis = {}
for r in res:
    # print(r,type(r))
    key = 'lijihua:'+ str(r['id'])
    dict_redis[key] = r['name']

# print(dict_redis)
#批量插入值到redis，需要传入字典
r_bd.mset(dict_redis)
#批量查询redis的值，需要传入元组
s = r_bd.mget(('lijihua:1','lijihua:2','lijihua:3'))
# print(s)


'''自增'''

#
import random
status_code = random.randint(200, 205)
# r_bd.mset({"success": 0, "fail": 0})
# print(r_bd.mget(("success", "fail")))
print(status_code)
if status_code == 200:
    r_bd.incr("lijihua:success") #若key值不存在时则创建
else:
    r_bd.incr("lijihua:fail")

print(r_bd.mget(("lijihua:success", "lijihua:fail")))


'''set集合查交集，并集'''
print(r_bd.sinter("circle:game:lol","circle:game:wzry"))
print(r_bd.sunion("circle:game:lol","circle:game:wzry"))