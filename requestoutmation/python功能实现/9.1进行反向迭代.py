l = [1, 2, 3, 4, 5]

#反转列表
l.reverse()
print(l)
print(l[::-1])

#反向迭代列表
l1 = reversed(l)
for i in l1:
    print(i)

"""
实现一个连续浮点数发生器FloatRange(和range类似)， 根据给定的范围（start, end）和步进值（step）产生一些连续浮点数
如迭代FloatRange(3.0, 4.0, 0.2)可产生序列

正向：3.0>3.2>3.4>3.6>3.8>4.0
反向：4.0>3.8>3.6>3.4>3.2>3.0
"""


class FloatRange:
    def __init__(self, start, end, step=0.1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):
        st = self.start
        while st <= self.end:
            yield st
            st += self.step

    def __reversed__(self):
        en = self.end
        while en >= self.start:
            yield en
            en -= self.step

fr = FloatRange(1.0, 5.0, 0.5)
for f1 in fr.__iter__():
    print(f1)
print('-' * 5)
for f2 in fr.__reversed__():
    print(f2)