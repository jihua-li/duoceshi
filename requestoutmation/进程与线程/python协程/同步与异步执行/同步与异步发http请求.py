import time
import gevent.monkey

gevent.monkey.patch_socket()
import gevent
import requests


def fetch(pid):
    response = requests.get('http://httpbin.org/get', timeout=50)
    print('请求结果 %s: %s' % (pid, response.status_code))
    return response.status_code


def synchronous():
    start = time.time()
    for i in range(1, 11):
        fetch(i)
    end = time.time()
    print("同步任务执行时间: {}".format(end - start))


def asynchronous():
    start = time.time()
    threads = []
    for i in range(1, 11):
        threads.append(gevent.spawn(fetch, i)) #创建协程列表
    gevent.joinall(threads) #添加协程
    end = time.time()
    print("异步任务执行时间: {}".format(end - start))

if __name__=='__main__':
    # print('同步执行:')
    # synchronous()
    print('异步执行:')
    asynchronous()
