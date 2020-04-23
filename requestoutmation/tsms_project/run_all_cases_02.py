import unittest
import os
# 来自：https://github.com/easonhan007/HTMLTestRunner
from tsms_project.commons.html_test_runner import BSTestRunner

curPath = os.path.realpath(__file__)
curDir = os.path.dirname(curPath)  # 获取父目录
casePath = os.path.join(curDir, "test_cases/sign_api")  # 拼接用例目录

# 查找全部用例，pattern是匹配规则，不传也可以
discover = unittest.defaultTestLoader.discover(start_dir=casePath, pattern='test*.py')

# 生成html报告
reportPath = os.path.join(curDir, "report", "report.html")
fp = open(reportPath, "wb")
runner = BSTestRunner(stream=fp, title="测试报告", description="简易描述")
runner.run(discover)
fp.close()
