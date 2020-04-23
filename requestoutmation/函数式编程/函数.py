#返回非多个值
def peson(name,age):
    name = name
    age = age
    return name, age

a = peson('carl',18)
# print(a)

#>>>>>>>>>>>>>>>>>>>>>>
def my_abs(x=1):
    '''计算绝对值'''
    if not isinstance(x, int):
        return None
    if x >= 0:
        return x
    else:
        return -x
# print(my_abs(0))
# print(my_abs(2))
# print(my_abs(-1))
# print(my_abs('henhao'))

#参数检查，程序自动报错不准确，可以手动抛出异常
def you_abs(x=1):
    if not isinstance(x, int):
        raise TypeError("传入的值类型必须是整型或浮点型")
    if x >= 0:
        return x
    else:
        return -x

# print(you_abs(x = 'a'))

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#返回多个参数，例如返回屏幕坐标
#导入math模块，以使用sin/cos函数
import math
#接受(x, y)起始坐标，step位移，angle角度(默认为0)
def move(x, y, step, angle= 0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny
#分开获取返回值
x, y = move(0,0,10,math.pi/6)
# print(x, y)
#获取返回元组
a = move(0,0,10,math.pi/6)
# print(a)
# print(a[0],a[1])

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
'''可变参数'''
#参数的个数不确定的时候，考虑把列表传进去，可变长可为0或多个
#加个*号就变可变长
def req_h(*user):
    for i in user:
        print(i)
a = ["duoceshi","carl","lijihua"]
#错误调用,输出整个列表
# req_h(a)
#正确调用，一个一个传
# req_h(a[0],a[1],a[2])
#或者使用*号，后面还可以添加
# req_h(*a)


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
'''关键字参数'''
#两个**号定义关键字参数
def person(name, age, **kw):
    print('name:',name, 'age:',age, 'other:', kw)

# extra = {'city': 'Shenzhen', 'job': 'Engineer', "home": "hunan"}
#错误调用
# person('duoceshi',4, extra)
#正确调用
# person('duoceshi', 4, city = extra['city'], job = extra['job'], home = extra['home'])
# person('duoceshi', 4, **extra)

'''命名关键字参数'''
#为了防止调用者传入不受限制的参数，命名关键字参数
#指定只接收特定的关键字参数，使用*分隔符
def person1(name, age, *, city = 'guangzhou', job):
    print(name, age, city, job)

# extra = {'job': 'Engineer'}
#传入不是指定的关键字参数，提示不接受该参数
# person1('duoceshi', 4, addr = 'nanshan')
#仅接受指定关键字参数
# person1('duoceshi', 4, **extra)

#如果已经包含了可变长参数，则不需要再加分割符
def person2(name, age, *args, city, job):
    print(name, age, args, city, job)

# extra = {'city': 'Shenzhen', 'job': 'Engineer'}
# person2('duoceshi', 4, *[1,2,3,4], **extra)

'''参数组合'''
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1(1, 2, 3, 'a', 'b', x=99)
#通过元组+字典调
f1(*(1, 2, 3, 'a', 'b'), **{"x": 99})
f2(1, 2, d=99, ext=None)


import random, string
def creat_str(num_int=0, num_letters=0, num_zh=0, num_pun=0):
    '''
    随机生成字符串，可以是：数字，字母，汉字，特殊字符的随机组合，可以指定某个单独字符类型出现次数
    :param num_int: 数字的个数
    :param num_letters: 字母的个数
    :param num_zh: 汉子的个数
    :param num_pun: 特殊字符的个数
    :return: 随机字符串，长度为传入参数只和
    '''
    ran_list = []
    for i in range(num_int):
        ran_list.append(random.choice((string.digits))) #随机获取0-9的数字
    for i in range(num_letters):
        ran_list.append(random.choice(string.ascii_letters)) #随机获取所有的英文字母
    for i in range(num_zh):
        ran_list.append(chr(random.randint(0x4e00, 0x9fbf))) #随机获取或有的汉字
    for i in range(num_pun):
        ran_list.append(random.choice(string.punctuation)) #随机获取所有的特殊字符
    random.shuffle(ran_list)
    return ''.join(ran_list)

# if __name__=='__main__':
    # random_str = creat_str(1,2,3,4)
    # random_str = creat_str(3,8)
    # print(random_str)

#递归函数：一个函数（方法）在自己内部调用自己本身
import sys
# sys.getrecursionlimit(100000)
def fact(i):
    '''计算阶乘'''
    if i == 1:
        return 1
    return i * fact(i - 1)
    # print(i * fact(i -1))
print(fact(5))
# fact(5)


# 格式化数据，即:接 请求后得到的结果
dcs = {
"name": "duoceshi",
"age": "4",
"grades1": {
    "number": 1,
    "teachers": ["pansir", "chensir"],
    "students": ["xiaohong", "xiaoming", "xiaobai"],
    "content": "python2"
},
"grades2": {
    "number": 2,
    "teachers": ["pansir", "chensir"],
    "students": ["tom", "jerry", "bob"],
    "content": "python3"
},
"grades3": {
    "number": 3,
    "teachers": ["pansir", "chensir"],
    "students": ["阿 ", "阿珍", "阿强"],
    "content": "java"
}}

#取出所有课程，组成列表
def get_content():
    all_stu = []
    #遍历所有字典的key
    for key in dcs:
        if 'grades' in key:
            print(key)
            all_stu.append(dcs[key]['content'])
    return all_stu

# gc = get_content()
# print(gc)

#当字段内容变更，str变字典，grades1变成level1，都会造成原有的方法不可用
#格式化数据，即：接口返回的结果
dcs1 = {
    "name": "duoceshi",
    "age": "4",
    "grades1": {
        "number": 1,
        "teachers": ["pansir", "chensir"],
        "students": ["xiaohong", "xiaoming", "xiaobai"],
        "content": {"theory": "auto-test", "language": "python2"}
    },
    "grades2": {
        "number": 2,
        "teachers": ["pansir", "chensir"],
        "students": ["tom", "jerry", "bob"],
        "content": {"theory": "auto-test", "language": "python3"}
    },
    "grades3": {
        "number": 3,
        "teachers": ["pansir", "chensir"],
        "students": ["阿 ", "阿珍", "阿强"],
        "content": {"theory": "auto-test", "language": "java"}
    }
}

# def get_content1():
#     all_stu = []
#     for key in dcs:
#         if 'grade' in key:
#             all_stu.append(dcs[key]['content']["language"])
#     return all_stu
# print(get_content1())

#3.引入递归来写一个通用方法，来解析任何字段，遍历多重字典，找到需要的key
dcs2 = {
    "name": "duoceshi",
    "age": "4",
    "grades1": {
        "number": 1,
        "teachers": ["pansir", "chensir"],
        "students": [{"shenzhen": "xiaohong"}, {"guangzhou": "xiaobai"}],
        "content": {"theory": "auto-test", "language": "python2"}
    },
    "grades2": {
        "number": 2,
        "teachers": ["pansir", "chensir"],
        "students": [{"shenzhen": "tom"}, {"guangzhou": "jerry"}],
        "content": {"theory": "auto-test", "language": "python3"}
    },
    "grades3": {
        "number": 3,
        "teachers": ["pansir", "chensir"],
        "students": [{"shenzhen": "阿珍"}, {"guangzhou": "阿强"}], "content": {"theory": "auto-test", "language": "java"}
        },
#  表下有 表， 表中再包含字典
    "extra": [[{"a": 1}, {"b": 2}], [{"a": "hello"}, {"b": "world"}]]
}

def get_exp(getkey, resdict):
    exp = []
    def get_value(get_key, res_dict):
        if isinstance(res_dict, dict):
            for k, v in res_dict.items():
                if k == getkey:
                    exp.append(v)
                get_value(get_key, v)
        if isinstance(res_dict, list):
            for ele in res_dict:
                get_value(get_key, ele)
    get_value(getkey, resdict)
    return exp

gv = get_exp('language', dcs2)
print(gv)


