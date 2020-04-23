import retrying, tenacity,logging


#场景案例
#若请求一个get接口，必须得到200，才能进行后续的操作，但该接口偶尔会返回非200
import random

# def add():
#     res = random.randint(200,205)
#     print("当前返回码是：{}".format(res))
#     assert res == 200
#
# #有概率执行失败，一旦失败，则终止
# add()

#通过try解决
#通过方法封装来实现
def add(retry = 4):
    res = random.randint(200,205)
    try:
        print(res)
        assert res ==200
    except:
        print(res)
        add()
# add()

#改造函数
def do_1(retry = 4):
    #指定循环次数
    for i in range(retry):
        try:
            #模拟随机返回码
            res = random.randint(200,202)
            #如果返回异常，则抛出异常
            if res != 200:
                raise IOError("Code is not 200, try again", res)
            else:
                #如果返回200，则返回
                print("get except result", res)
                return res
        except Exception as err:
            #捕获刚刚抛出的异常
            print(err)
# d = do_1()
# print(d)

'''>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'''
#通过装饰器
#用函数不太方便，单个实现尚可，若用例/程序中大量使用，则无法满足
import logging, random, time
from functools import wraps

logging.basicConfig(level=logging.INFO, format='%(asctime)-16s %(levelname)-8s %(message)s')

#定义装饰器，带参数则是三层嵌套
def retry_test(func):
    #复制元信息
    @wraps(func)
    def wrapped(*args, **kwargs):
        last_raised = None
        #定义尝试次数，这里写死
        retry_limit = 3
        for i in range(retry_limit):
            try:
                return func(*args, **kwargs)
            except Exception as err: #普获异常
                print(err)
                last_raised = err
        if last_raised:
            raise last_raised
    return wrapped

# @retry_test
# def add():
#     #模拟随机获取的http返回码
#     res = random.randint(200, 205)
#     print("当前返回码为：{}".format(res))
#     assert res == 200

# add()

'''>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'''
#带参数装饰器
# def do_retry(retry_time= 3, delay_seconds= 0):
#     '''
#     带参数错误重试装饰器,通过参数指定重试次数，重试的间隔时间
#     :param retry_time: 重试次数
#     :param delay_seconds: 重试间隔
#     :return: 被装饰函数返回结果
#     '''
#     #当在wrapper的局部作用于里面操作不可变类型的数据时，会生成成新的局部变 ，但是是新生成的局部变 retry_times在使用时还没来得及初始化，因此会提示找不到变量。
#     #将不可变参数用可变容器封装即可，即:闭包下如何捕获变
#     temp_dict = {
#         'retry_time':retry_time,
#         'delay_seconds':delay_seconds
#     }
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             last_err = None
#             retry_time = temp_dict.get('retry_time')
#             delay_seconds = temp_dict.get('delay_seconds')
#             # for i in range(retry_time):
#             while retry_time > 0:
#                 try:
#                     return func(*args, **kwargs)
#                 except Exception as err: #捕获异常
#                     # logging.warn(err)
#                     # print(err)
#                     last_err = err
#                     if delay_seconds > 0:
#                         time.sleep(delay_seconds)
#                     #重试次数-1
#                     retry_time -= 1
#             #如果last_err不为空，则抛出异常
#             if last_err:
#                 raise last_err
#         return wrapper
#     return decorator



'''>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'''
#最终版本
def do_retry(retry_time= 1, delay_seconds= 0):
    '''
    带参数错误重试装饰器,通过参数指定重试次数，重试的间隔时间
    :param retry_time: 重试次数
    :param delay_seconds: 重试间隔
    :return: 被装饰函数返回结果
    '''
    temp_dict = {
        'retry_time':3 if retry_time < 0 or retry_time > 5 else retry_time, #retry_time小于0次或大于5次，则取3次
        'delay_seconds':2 if delay_seconds < 0 or delay_seconds > 5 else delay_seconds #delay_seconds小于0次或大于5次，则取3次
    }
    def decorator(func):
        #复制元信息
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_err = None
            retry_time = temp_dict.get('retry_time')
            delay_seconds = temp_dict.get('delay_seconds')

            while retry_time > 0:
                try:
                    return func(*args, **kwargs)
                except Exception as err:
                    last_err = err
                    if delay_seconds > 0:
                        time.sleep(delay_seconds)
                    #重复次数-1
                    retry_time -= 1
            #如果last_err不为空，则抛出异常
            if last_err:
                raise last_err
        return wrapper
    return decorator

@do_retry(6)
def add1():
    #模拟随机获取的http返回码
    res = random.randint(200, 205)
    print("当前返回码为：{}".format(res))
    assert res == 200

add1()
