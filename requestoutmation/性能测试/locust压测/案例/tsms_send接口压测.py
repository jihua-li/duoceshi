import json
import logging, sys
import queue
import re

import requests
from locust import TaskSet, task, HttpLocust

logging.basicConfig(level=logging.INFO, format='%(asctime)-16s %(levelname)-8s %(message)s')
sys.path.append("../01advanced_course/test_tsms_project/tsms_pytest_commons")
sys.path.append("../01advanced_course/test_tsms_project")
from tsms_base import TsmsBase


class UserSign(TaskSet):
    def on_start(self):
        self.ts = TsmsBase()
        self.auth = ("dcs", "123")

    @task
    def test_register(self):
        data = {
            "sign_id": 16,
            "temp_id": 6,
            "mobiles": self.ts.gen_phones(1)
        }
        with self.client.post("/v1/message", json=data, auth=self.auth, catch_response=True) as res:
            # logging.info(res.status_code)
            # logging.info(res.text)
            if res.status_code == 200 and "uuid" in json.loads(res.text):
                res.success()
            else:
                res.failure("[response fail]: {} {}".format(res.status_code, res.text))


class WebsiteUser(HttpLocust):
    host = "http://www.captaintests.club"
    task_set = UserSign
    min_wait = 0
    max_wait = 0