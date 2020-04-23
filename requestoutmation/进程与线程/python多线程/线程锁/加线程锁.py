import time, threading

"""
多进程:每个进程独享一个变量，各进程间互相影响
多线程:所有变化由所有线程共享，任何线程都可以修改，存在同时修改一个变量情况，导致变量错乱

锁的优点与缺点
优点:某段关键代码，只能由一个线程从头到尾执 ，保证数据准确
缺点:
1. 线程不能并发 
2. 出现死锁
"""

lock = threading.Lock()

balance = 0
def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(1000000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()

if __name__ =='__main__':
    t1 = threading.Thread(target=run_thread, args=(5,))
    t2 = threading.Thread(target=run_thread, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(balance)
