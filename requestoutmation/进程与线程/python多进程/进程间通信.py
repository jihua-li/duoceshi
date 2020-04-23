from multiprocessing import Process, Queue
import os, time, random


def write(q):
    print('执行写操作的进程id: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('往队列写入 %s ...' % value)
        q.put(value)
        time.sleep(random.random())


def read(q):
    print('执行读操作的进程id: %s' % os.getpid())
    while True:
        value = q.get(True) #参数True表示队列里面的值都取完了就等待
        print('从队列读取 %s .' % value)


if __name__ == '__main__':
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()
