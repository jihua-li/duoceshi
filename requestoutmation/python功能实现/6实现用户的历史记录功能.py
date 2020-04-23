from random import randint
from collections import deque
import pickle #可以将一个python对象存储到文件当中


n = randint(1, 100)
#创建一个双尾队列，并声明队列长度
history = deque([], 5)


def guess(k):
    if k == n:
        print('right')
        return True
    elif k < n:
        print('{} is less-than guess number'.format(k))
        return False
    else:
        print('{} is greater-than guess number'.format(k))
        return False

while True:
    history = pickle.load(open(r'history', 'rb'))
    line = input('Please input you number:')
    if line.isdigit():
        k = int(line)
        history.append(k)
        pickle.dump(history, open(r'history', 'wb'))
        if guess(k):
            break
    elif line == 'history' or line == 'h?':
        print(history)
    elif line == 'exit':

        print('退出游戏')
        break
    else:
        print('必须输入数字！！！')

