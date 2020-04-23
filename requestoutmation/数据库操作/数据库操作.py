'''pymysql'''
import pymysql

'''db_config =''
#连接数据库
db = pymysql.connect(db_config)

sql = ''
#获取游标
crusor = db.cursor()
#执行sql
crusor.execute(sql)'''

db_config = {
    'host':'192.168.0.148',
    'port':3306,
    'user':'root',
    'password':'123456',
    'db':'flaskblog',
    'charset':'utf8mb4'
}
#连接数据库
# db = pymysql.connect(**db_config)
#获取游标
# cursor = db.cursor()

#执行sql
# res = cursor.execute('select * from sms_sign where sign_user_id = 16 and audit_status = "passed"')
# print(cursor.fetchall())#取所有数据
# print(cursor.fetchone()) #取单条数据
# print(cursor.fetchmany(1)) #获取前n条数据
# print(cursor.fetchone()[0])


'''records'''
#推荐使用，很强大
import records, random
from tsms_project.commons.tsms_base import Tsmstest

ts = Tsmstest()

# db = records.Database('mysql+pymysql://root:123456@192.168.0.171:3306/flaskblog?charset=utf8')
#
# res = db.query('select * from sms_sign where sign_user_id = 16 and audit_status = "passed"')
# print(res)
# print(list(res))
# print(list(map(dict, list(res)))) #将list中的值统一转换成dict,并以list的格式输出
# print([dict(r) for r in list(res)])
# for r in list(res):
#     print(dict(r))

'''删除表'''
# sql_del_table = 'DROP TABLE lijihua'
# res0 = db.query(sql_del_table)

'''创建表'''
# sql_create_table = 'CREATE TABLE if NOT EXISTS lijihua(name varchar(20), age int) default charset = utf8'
# res1 = db.query(sql_create_table)

'''插入表数据'''
#常用方法
# sql_insert_data = 'INSERT INTO lijihua(name, age) VALUES ("{}",{})'.format('carl',20)
# res2 = db.query(sql_insert_data)
# print(res2)
#records自带的语法
user = {'name':'xiaoming','age':19}
# db.query('INSERT INTO lijihua(name, age) VALUES(:name,:age)',**user) #(:name,:age)中的命名对应user中的keys

list_1 = []
#造数据
# for i in range(100):
#     list_1.append({'name':ts.gen_ranstr(0,5), 'age':random.randint(0,100)})

#一次性插入多条数据
users = [
    {'name':'xiaoxiao','age':21},
    {'name':'xiaohong','age':22},
    {'name':'xiaodong','age':23}
]
# db.bulk_query('INSERT INTO lijihua(name, age) VALUES(:name,:age)',users)
# db.bulk_query('INSERT INTO lijihua(name, age) VALUES(:name,:age)',list_1)

'''查询数据'''
# sql_select_data = 'select * from lijihua'
# rows = db.query(sql_select_data)
#返回所有数据
# print(rows.all())
#以字典的格式返回所有数据
# print(rows.all(as_dict=True))
#返回第一条数据
# print(rows.first())
#以字典的格式返回第一条数据
# print(rows.first(as_dict=True))
#以排序字典的格式返回第一条数据
# print(rows.first(as_dict=True))
#查询唯一的一个，必须唯一一个记录，才能执行通过
# print(rows.one())

#返回json,yaml,html,xls,csv格式数据
# print(rows.export('json'))
# print(rows.export('yaml'))
# print(rows.export('html'))
# print(rows.export('xls'))
# print(rows.export('csv'))

'''以xlsx格式返回数据，并写入到Excel'''
# rows = db.query('select * from sms_sign where sign_user_id = 16 order by sign_id DESC')
# # print(rows.export('xlsx'))
# with open('signdata.xlsx', 'wb') as f:
#     f.write(rows.export('xlsx'))
#     print('ok')

'''数据库的事务性'''
#通过transaction获取一个事物对象


'''3. 完成一个方法，该方法可以修改指定表的指定字段的值 
要求:
1. 只允许修改 audit_status 字段
2. 参考定义: def tsms_update(self, table, field, value, **kwargs): 
思 :先写一条sql，然后从调用者的角度去思考怎么剥离变量'''


'''业务删除表数据'''
from tsms_project.commons.tsms_db import OperationDb

od = OperationDb()
od.tsms_record_del("sms_sign", sign_id = 158)
res3 = od.tsms_select("sms_sign", "is_delete", sign_id = 158)
print(res3)