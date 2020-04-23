import json
import logging, sys
import queue
import re

import requests
from locust import TaskSet, task, HttpLocust

logging.basicConfig(level=logging.INFO, format='%(asctime)-16s %(levelname)-8s %(message)s')
sys.path.append("../test_tsms_project/tsms_pytest_commons")
sys.path.append("../test_tsms_project")
from tsms_base import TsmsBase


class UserSign(TaskSet):
    def on_start(self):
        self.ts = TsmsBase()
        self.auth = ("dcs", "123")

    @task
    def test_register(self):
        data = {
            "signature": self.ts.gen_ranstr(3, 3),
            "source": self.ts.gen_ranstr(5, 5),
            "pics": []
        }
        with self.client.post("/v1/signature", json=data, auth=self.auth, catch_response=True) as res:
            # logging.info(res.status_code)
            # logging.info(res.text)
            if res.status_code == 200 and "sign_id" in json.loads(res.text):
                res.success()
            else:
                res.failure("[unknow fail]: {} {}".format(res.status_code, res.text))


class WebsiteUser(HttpLocust):
    host = "http://www.captaintests.club"
    task_set = UserSign
    min_wait = 0
    max_wait = 0