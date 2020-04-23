import threading

"""
1. local_school.student是局部变量，线程自己独享
2. 常用场景:每个线程绑定一个数据库连接，HTTP请求，用户身份信息
"""

local_school = threading.local()


def process_student():
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))


def process_thread(name):
    local_school.student = name
    for i in range(20):
        process_student()

if __name__ =='__main__':
    t1 = threading.Thread(target=process_thread, args=('liudan',), name='Thread-A')
    t2 = threading.Thread(target=process_thread, args=('shangcl',), name='Thread-B')
    t1.start()
    t2.start()
    t1.join()
    t2.join()
