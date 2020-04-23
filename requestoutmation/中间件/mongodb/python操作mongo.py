from pymongo import MongoClient



client = MongoClient("mongodb://148.70.194.135:27017/")
db = client.box
col = db.box

"""插入"""
test_data1 = {
    "name": "lijihua",
    "info": {"age": 18, "six": "M", "hehe": None}
}
test_data2 = {
    "name": "carl",
    "six": "man"
}

#插入单条
# res1 = col.insert_one(test_data1)
# print(res1.inserted_id)

#插入多条
# res2 = col.insert_many([test_data1, test_data2])
# print(res2.inserted_ids)


"""查询"""
#1、按条件默认返回第一个
# res = col.find_one({"name": "lijihua"})
# print(res)

#2、查找全部
# res = col.find()
# for i in res:
#     print(i)

#3、按条件查询多条
# res = col.find({"name":"lijihua"})
# for i in res:
#     print(i)

#4、查询年龄大于18
# res = col.find({"age": {"$gt": 18}})
# for i in res:
#     print(i)

#5、正则匹配
# res = col.find({"name": {"$regex": "^li.*"}})
# for i in res:
#     print(i)

#6、属性是否存在，查询包含指定字段的数据
# res = col.find({"age": {"$exists": True}})
# for i in res:
#     print(i)

#7、查询指定数据类型
res = col.find({"age": {"$type": 1}})
for i in res:
    print(i)