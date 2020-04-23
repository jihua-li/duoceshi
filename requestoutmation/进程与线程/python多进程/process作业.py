import logging, requests
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)-16s %(levelname)-8s %(message)s')
from multiprocessing import Process, Pool
from tsms_pytest_commons.tsms_base import TsmsBase

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


def main1():
    # 多进程
    start = time.time()
    #创建进程池
    p = Pool(1)
    for i in range(8):
        p.apply_async(task, args=())
    p.close()
    p.join()
    end = time.time()
    logging.info("[time is]: {}".format(end - start))


def main2():
    # 单进程
    start = time.time()
    for i in range(8):
        task()
    end = time.time()
    logging.info("[time is]: {}".format(end - start))


if __name__ == '__main__':
    main1()
    # main2()
    # task()