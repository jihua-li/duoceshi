from time import time
from collections import OrderedDict
from random import randint

dic = OrderedDict()
players = list('ABCDEFGH')

start = time()
for i in range(1, 9):
    input('请按回车键确认完成>>')
    p = players.pop(randint(0, 8-i))
    end = time()
    print(i, p, end - start)
    dic[p] = (i, end - start)

for k, v in dic.items():
    print(k, v)