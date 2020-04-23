from gevent import monkey;monkey.patch_all()
import logging, requests, time, gevent
from multiprocessing import Pool, Process
from tsms_pytest_commons.tsms_base import TsmsBase

logging.basicConfig(level=logging.INFO, format='%(asctime)-16s %(levelname)-8s %(message)s')

ts = TsmsBase()


def task():
    url = "http://www.captaintests.club/v1/message"
    data = {
        "sign_id": 16,
        "temp_id": 6,
        "mobiles": ts.gen_phones(1)
    }
    user = "dcs"
    password = "123"
    res = requests.post(url, json=data, auth=(user, password))
    logging.info(res.status_code)
    return res.text

def main1():
    """进程加协程并发"""
    logging.info('main函数开始执行')
    starttime = time.time()
    p = Pool(8)
    for i in range(8):
        p.apply_async(task, args=())
    logging.info('多进程执行完成')
    p.close()
    p.join()
    endtime = time.time()
    logging.info('time is: {}'.format(endtime - starttime))

def main2(num):
    """协程并发"""
    starttime = time.time()
    jobs = [gevent.spawn(task) for i in range(int(num))]
    gevent.joinall(jobs)
    endtime = time.time()
    logging.info("执行时间：{}".format(endtime - starttime))
    logging.info("[tps is]: {}".format(num / (end - start)))
    logging.info("task函数返回结果：{}".format([job.value for job in jobs]))

def main3(num):
    start = time.time()
    p1 = Process(target=main2, args=(num / 2,))
    p2 = Process(target=main2, args=(num / 2,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end = time.time()
    logging.info("[process + gevent tps is]: {}".format(num / (end - start)))



if __name__=='__main__':
    # starttime = time.time()
    # jobs = [gevent.spawn(main1)]
    # print(jobs)
    # gevent.joinall(jobs, timeout=5)
    # endtime = time.time()
    # print("总耗时：{}".format(endtime - starttime))
    # task()
    main2(20)