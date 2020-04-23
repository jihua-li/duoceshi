"""
生成器函数就是包含yield语句的函数

实现一个可迭代对象的类，他能迭代出给定范围内的所有素数
曾称质数。一个大于1的正整数，如果除了1和它本身以外，不能被其他正整数整除，就叫素数。如2，3，5，7，11，13，17…。
"""

import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)16s - %(levelname)8s - %(message)s')

def f():
    print('in f(), 1')
    yield 1

    print('in f(), 2')
    yield 2

    print('in f(), 3')
    yield 3

g = f()
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
# for g in f():
#     print(g)

class PrimeNumber():
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def isprimenum(self, k):
        if k < 2:
            return False
        for i in range(2, k):
            if k % i == 0:
                return False
        return True

    def __iter__(self):
        for k in range(self.start, self.end + 1):
            if self.isprimenum(k):
                yield k

if __name__ =='__main__':
    p = PrimeNumber(1, 100)
    pl = [i for i in p]
    print(pl)