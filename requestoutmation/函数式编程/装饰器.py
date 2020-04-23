# 最终版本
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)-16s %(levelname)-8s %(message)s')
#基础型装饰器

def use_logging(func):
    def wrapper(*args, **kwargs):
        logging.info("[当前调 的函数是]: {}".format(func.__name__))
        for i in range(len(args)):
            logging.info("[第{}个参数是]: {}".format(i, args[i]))
        for k, v in kwargs.items():
            logging.info("key is: {}  value is: {}".format(k, v))
        return func(*args, **kwargs)
    return wrapper



@use_logging
def add(a, b):
    c = a + b
    return c


# ad = add(a=1, b=44)
# print(ad)

'''--------------------------'''

#参数型装饰器
# 再封装一层，用来带参数
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
ad = add(1, 44)

print(ad)


'''装饰器进阶'''

# 构建装饰器
import functools
def params_check1(*types, **kwtypes):
    def decorator(func):
        @functools.wraps(func)  # 保留元信息
        def wrapper(*args, **kwargs):
            # 判断可变长参数
            res1 = [isinstance(para, type) for para, type in zip(args, types)]
            assert all(res1), "args type is not expect"
            # 判断关键字参数
            res2 = [isinstance(kwargs[key], kwtypes[key]) for key in kwargs]
            assert all(res2), "keyword para is not expect"
            return func(*args, **kwargs)

        return wrapper

    return decorator

# 使用装饰器，注意：这里的参数名必须和函数定义一致
@params_check1(int, str, c=(int, str))
def test(a, b, c):
    print("执行函数 test, a=%s, b=%s, c=%s" % (a, b, c))
    return "hello"

# 测试用例
# print(test(1, "str", c=1))  # 参数正确

#练习，写一个简单的装饰器，计算函数的执行时间
import time

#拓展：函数调用基数，函数计时，

#类装饰器
