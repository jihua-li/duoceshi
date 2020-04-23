import json
import logging, sys
import queue
import re

import requests
from locust import TaskSet, task, HttpLocust

logging.basicConfig(level=logging.INFO, format='%(asctime)-16s %(levelname)-8s %(message)s')


class UserSign(TaskSet):
    def on_start(self):
        self.reg_url = "http://www.captaintests.club/login"
        res = requests.get(self.reg_url, allow_redirects=False)
        pat = re.compile('''<input id="csrf_token" name="csrf_token" type="hidden" value="(.*?)">''', re.S)
        self.token = re.findall(pat, res.text)[0]
        self.ck = res.cookies
        logging.info("[token is]: {}".format(self.token))
        logging.info("[cookie is]: {}".format(self.ck))
        data = {
            "username": "dcs",
            "password": "123",
            "csrf_token": self.token
        }
        self.client.post("/login", data=data, cookies=self.ck)

    @task
    def test_register(self):
        with self.client.get("/user/dcs/sign", catch_response=True) as res:
            # logging.info(res.status_code)
            # logging.info(res.text)
            if res.status_code == 200 and "16" in res.text:
                res.success()
            else:
                res.failure("[unknow fail]: {} {}".format(res.status_code, res.text))


class WebsiteUser(HttpLocust):
    host = "http://www.captaintests.club"
    task_set = UserSign
    min_wait = 0
    max_wait = 0