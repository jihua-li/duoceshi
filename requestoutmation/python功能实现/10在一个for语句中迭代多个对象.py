from random import randint
from itertools import chain

#并行, 统计每个同学三门学科的总成绩, zip(list1, list2, list3)按顺序将三个列表中的值以元组的形式组成一个新的列表,并向短的看齐
# 例如list1 = [1,2,3]，list2=['a','b','c'], list3=['h','k']
#那么通过zip(list1, list2, list3)就会组成一个新的列表 [(1, 'a', 'h'), (2, 'b', 'k')], 因为其中的list3只有两个元素，所以其他
#列表中多余两个元素的值被丢弃
chinese = [randint(50, 100) for _ in range(40)]
math = [randint(50, 100) for _ in range(40)]
english = [randint(50, 100) for _ in range(40)]

total = []
for c, m, e in zip(chinese, math, english):
    total.append(c + m + e)

print(total)

#串行，统计三个班中成绩大于90分的人数 ，chain(list1, list2, list3)将三个列表串起来迭代
b1 = [randint(50, 100) for _ in range(38)]
b2 = [randint(50, 100) for _ in range(40)]
b3 = [randint(50, 100) for _ in range(45)]

count = 0
for i in chain(b1, b2, b3):
    if i > 90:
        count += 1

print(count)