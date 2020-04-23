import random, timeit

"""列表"""
#生成10个-10到10的随机数字
data = [random.randint(-10, 10) for _ in range(10)]
print(data)

#筛选数据
#方法一 迭代
new_data1 = []
for i in data:
    if i >= 0:
        new_data1.append(i)
print(new_data1)

#方法二 filter()
new_data2 = list(filter(lambda x: x >= 0, data))
print('filter()运行时间：{}'.format(timeit.timeit(stmt='new_data2', setup='from __main__ import new_data2', number=1)))
print(new_data2)


#方法三 列表解析
new_data3 = [x for x in data if x >= 0]
print('列表解析运行时间：{}'.format(timeit.timeit(stmt='new_data3', setup='from __main__ import new_data3', number=1)))

print(new_data3)



"""字典"""

dic = {x: random.randint(60, 100) for x in range(1, 21)}
print(dic)

#字典解析
new_dic = {k: v for k, v in dic.items() if v >= 90}
print(new_dic)


"""集合"""
#将列表转换为集合
s = set(data)
print(s)

#集合解析
new_s = {i for i in s if i % 3 == 0}
print(new_s)