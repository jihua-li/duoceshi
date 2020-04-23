#变量可以指向函数
x = abs(-100)
# print(x)

#一个函数可以接受另一个函数作为参数，这种函数叫做高阶函数
def add(x, y, f):
    return f(x)+f(y)
z = add(-10, -20, abs)
# print(z)

#内建高价函数
# map() #对可迭代对象进行统一操作，接收两个参数，第 一个是函数，第二个是可迭代对象
#1/将一个列表所有的数据转换成字符串
a = [1,2,3,4,5,6]
b = []
for i in a:
    b.append(str(i))
print(b)

d = [7,8,9]
#map()
c = map(str, a)
print(c)
print(list(c))

#2/把不规范的英 文名字，改成大写开头的规范名字
def modify_name(name):
    return name[0].upper() + name[1:].lower()
# a = 'cArl'
# print(modify_name(a))

names = ['cArl','LIJIhua','liMING']
m = map(modify_name, names)
print(list(m))


# filter() #过滤和筛选元素,接收一个函数，和一个可迭代对象
#作用:将可迭代对象依次传入该函数，通过返回值是True还是False决定去

#筛选大于5的数
a = [1,2,3,4,5,6,7,8]
def filt(x):
    if x > 5:
        return True

# filter过滤，当 满 条件当时候，函数return None，filter判断为False，则不取该元素
c = filter(filt, a)
print(list(c))
# sorted() #排序
#
# lambda x: x[1] #匿名函数，等价于
# def ll(x):
#     return x[1]


#1.3 返回函数
#作用域
#嵌套函数
#闭包,避免使用全局变量
#匿名函数 lambda,一般与高阶函数配合使用

#求出1-20的奇数
def car_number(x):
    return x % 2 != 0
    # if x % 2 != 0:
    #     return True

a = list(filter(lambda x: x%2 != 0, range(1, 21)))
# print(a)

#装饰器 @语法糖
#基础型装饰器
#参数型装饰器
#判断参数型装饰器
#loging模块 critical/error/info/debug

# 最终版本
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)-16s %(levelname)-8s %(message)s')

# 再封装 层， 来带参数
def use_logging(level):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if level == 'info':
                logging.info("[当前调 的函数是]: {}".format(func.__name__))
                for i in range(len(args)):
                    logging.info("[第{}个参数是]: {}".format(i, args[i]))
                for k, v in kwargs.items():
                    logging.info("key is: {}  value is: {}".format(k, v))
                return func(*args, **kwargs)
        return wrapper
    return decorator


@use_logging("info")
def add(a, b):
    c = a + b
    return c


# ad = add(a=1, b=44)
# print(ad)

