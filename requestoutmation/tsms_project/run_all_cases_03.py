import unittest, time
import os
# 来自：https://github.com/easonhan007/HTMLTestRunner
from tsms_project.commons.html_test_runner import BSTestRunner

# 获取父路径
curPath = os.path.dirname(os.path.realpath(__file__))


def add_case(caseName="test_cases", rule="test*.py"):
    '''加载所有测试用例'''
    # 用例文件夹
    casePath = os.path.join(curPath, caseName)
    # 文件夹不存在则新建一个
    if not os.path.exists(casePath):
        os.mkdir(casePath)
    # 定义discover方法的参数
    discover = unittest.defaultTestLoader.discover(start_dir=casePath, pattern=rule, top_level_dir=None)
    return discover


def run_case(all_case, repotName="report"):
    # 执行路径下所有测试用例
    now = time.strftime("%Y_%m_%d_%H_%M_%s")
    # 报告文件夹
    reportPath = os.path.join(curPath, repotName)
    # 若报告文件夹不存在，则新建一个
    if not os.path.join(reportPath):
        os.mkdir(reportPath)
    report_abspath = os.path.join(reportPath, "result.html")
    fp = open(report_abspath, "wb")
    runner = BSTestRunner(stream=fp, title="测试报告", description="此报告为tsms系统接口测试报告")
    runner.run(all_case)
    fp.close()


if __name__ == '__main__':
    # 获取用例
    all_cases = add_case()
    # 执行用例
    run_case(all_cases)
