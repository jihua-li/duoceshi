#类装饰器3中类型
#1.内外层都不带参数的装饰器，写法@get_time
#2.装饰器带参数，函数不带参数的装饰器，
#3.类装饰器不带参数，被修饰对象带参数
#4.类装饰器和被装饰对象，都带参数，完全体

'''1'''
import logging
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)-16s %(levelname)-8s %(message)s')

class get_time(object):
    '''计算函数执行时间装饰器'''
    def __init__(self, func):
        self.__func = func

    def __call__(self, *args, **kwargs):
        logging.info("[当前调用的函数是]：{}" .format(self.__func.__name__))
        start_time = time.time()
        result = self.__func()
        end_time = time.time()
        print('函数执行时间为：%.10f' % (float(end_time - start_time)))
        return result

@get_time
def add():
    print('Are you ok ?')

add()