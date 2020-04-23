import time, threading


def loop():
    print('当前执行的线程是: %s ' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('线程 %s >>> 迭代 %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('当前线程 %s 执行结束.' % threading.current_thread().name)



if __name__ =='__main__':
    print('当前执行的线程是: %s ' % threading.current_thread().name)
    t1 = threading.Thread(target=loop, name='LoopThread1')
    t2 = threading.Thread(target=loop, name='Loop2')
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('当前线程 %s 执行完毕.' % threading.current_thread().name)