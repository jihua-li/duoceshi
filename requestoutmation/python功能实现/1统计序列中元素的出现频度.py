
#1、某随机序列中[12,3,4,5,6,5,6,7,7,8,2,1,2,9,0,4...]，找出出现次数最高的3个元素，他们出现的次数是多少？

import random
#随机生成30个-10到10之间的数字
l1 = [random.randint(-10, 10) for _ in range(30)]
print(l1)

#统计频度
#方法一：把列表 l1 作为键，把出现的次数作为值  ，传入字典  。 使用字典的fromkeys方法
c = dict.fromkeys(l1, 0)
print(c)
for one in l1:
    c[one] +=1
print(c)

#方法二：专门处理计数问题的方法  。使用collections.Counter方法
from collections import Counter
#通过Counter方法统计统计列表中每个数字出现的次数
l2 = Counter(l1)
print(l2, type(l2))
#统计出现过3次的数字
print(l2.most_common(3))

"""统计英文单词的词频"""
import re

with open(r'./test.Text', 'r') as file: #打开文件 统计readme.txt中的单词词频
    text = file.read() #把文件读取的内容变成字符串 ，因为re,split 方法的参数接受的是字符串 而不是列表
    l3 = re.split('\W+', text) #  \W+是把字符串按照非字母的来分隔
    l4 = Counter(l3)
    print(l4)
    print(l4.most_common(3))
