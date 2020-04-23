""""所谓公共键就是只在每个字典中都出现的键（key）"""

from random import randint, sample
from functools import reduce

#随机取样, 生成一个字典
s = sample('abcdefg', randint(3, 7))
print(s)

#从abcdefg 中随机取出 3-6个，作为key， 1-4 的随机数作为 value
s1 = {x: randint(1, 4) for x in sample('abcdefg', randint(3, 6))}
print(s1)

s2 = {'a': 3, 'f': 3, 'd': 3, 'c': 3, 'b': 1}
s3 = {'c': 4, 'e': 4, 'd': 2, 'a': 2, 'f': 1, 'b': 2}
s4 = {'a': 4, 'c': 2, 'g': 4, 'd': 4, 'f': 1, 'b': 3}

#方法一， 集合方法
print(s2.keys() & s3.keys() & s4.keys())


#方法二，使用map和reduce
res = reduce(lambda x, y: x & y, map(dict.keys, [s2, s3, s4]))
print(res)
