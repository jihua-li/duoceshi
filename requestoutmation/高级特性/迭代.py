#通过for循环遍历tuple或list，叫迭代
# dict也可以迭代

# for i in range(10):
#     print(i)

# for i in (0,10):
#     print(i)


# d = {"name": "duoceshi", "age": 4, "score": 99}
# #仅迭代key
# for key in d:
#     print(key)
#
# #仅迭代value
# for value in d.values():
#     print(value)
#
# #同时迭代
# for k, v in d.items():
#     print(k, v)


#字符串也可以迭代
# for i in 'hellokitty':
#     print(i)

#判断对象是否可以迭代
# from collections import Iterable
# print(isinstance('abc', Iterable))
# print(isinstance(('a','b','c'), Iterable))
# print(isinstance(123,Iterable))

#遍历列表时改为元素对
a = ['A', 'B', 'C']
for i in range(len(a)):
    print(i, a[i])

for i, value in enumerate(a):
    print(i, value)

#小结: 任何可迭代对象都可以作用于for循环，包括我们自定义的数据类型，只要符合迭代条件， 就可以使用for循环。


