from collections import Iterable
import random, string

'''判断对象是否为可迭代对象'''
# print(isinstance('abc',Iterable))


#列表生成式
b = []
b = [i * i for i in range(1, 11) if i % 2 == 0]
# print(b)

#嵌套两层循环
d = [a + b for a in 'abc' for b in 'xyz']
# print(d)


#随机生成字符--列表生成式
def create_str2(num_int=0, num_letters=0, num_zh=0, num_pun=0):
    a = [random.choice(string.digits) for i in range(int(num_int))]
    b = [random.choice(string.ascii_letters) for i in range(int(num_letters))]
    c = [chr(random.randint(0x4e00, 0x9fbf)) for i in range(int(num_zh))]
    d = [random.choice(string.punctuation) for i in range(int(num_pun))]
    ran_list = a + b + c + d
    random.shuffle(ran_list)
    return ''.join(ran_list)
a = create_str2(1,2,3,4)
# print(a)


import re
a = ['aababbc','badabcab']
b = [re.sub(r'ab','', i) for i in a]
print(b)

# 计划用量
WTPLAN = 100
# 实际用量
WTQNT = 130
# 单价
WTPRC0 = 1
WTPRC1 = 2
WTPRC2 = 3


def charge(WTQNT, WTPLAN):
    try:
        if int(WTPLAN) < 0 or WTQNT < 0:
            print("param must be int")
            return
    except Exception as e:
        print(e)
        return
    if WTQNT <= WTPLAN:
        expr = WTQNT * WTPRC0
    elif WTQNT <= WTPLAN * 1.2:
        expr = WTPLAN * WTPRC0 + (WTQNT - WTPLAN) * WTPRC1
    else:
        expr = WTPLAN * WTPRC0 + WTPLAN * 0.2 * WTPRC1 + (WTQNT - WTPLAN * 1.2) * WTPRC2
    return expr


# a = charge(130, 100)
# print(a)

def split_fun(a):
    print(a.split(' '))

a = 'dsf ajdkf aljd'
split_fun(a)
print(sorted(split_fun(a)))