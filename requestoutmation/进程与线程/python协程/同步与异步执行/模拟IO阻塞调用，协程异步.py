import time, gevent
from gevent import select


"""模拟IO阻塞调用，协程异步"""
start = time.time()
tic = lambda: '时间差为: %1.1f' % (time.time() - start)

def gr1():
    print('gr1开始轮询: %s' % tic())
    select.select([], [], [], 2)
    print('gr1结束轮询: %s' % tic())
def gr2():
    print('gr2开始轮询时间: %s' % tic())
    select.select([], [], [], 2)
    print('gr2结束轮询: %s' % tic())
def gr3():
    print("gr3执行时间, %s" % tic())
    gevent.sleep(1)
    print("gr3执行完毕, %s" % tic())

if __name__ =='__main__':
    gevent.joinall([
        gevent.spawn(gr1),
        gevent.spawn(gr2),
        gevent.spawn(gr3),
    ])