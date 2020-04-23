# from multiprocessing import Pool
from multiprocessing import Pool
import os, time, random



def long_time_task(name):
    print("执行任务 {} ({})".format(name, os.getpid()))
    starttime = time.time()
    time.sleep(random.random()*3)
    endtime = time.time()
    print("任务 %s 执行了 %0.2f 秒" % (name, (endtime - starttime)))

if __name__ =='__main__':
    print("当前进程的父任务ID {}".format(os.getpid()))
    p = Pool(5)
    for i in range(4):
        p.apply_async(long_time_task, args=(i,))
    print("等待所有子进程加载....")
    p.close()
    p.join()
    print("所有子进程执行完毕")

