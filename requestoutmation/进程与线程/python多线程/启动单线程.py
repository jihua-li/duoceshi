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
    t = threading.Thread(target=loop, name='LoopThread')

    t.start()
    t.join()
    print('当前线程 %s 执 完毕.' % threading.current_thread().name)