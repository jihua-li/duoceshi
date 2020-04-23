import unittest
import os

# 绝对路径，写死不太好，例如，你在测试机器上运行，则会报错
# casePath = '/Users/panwj/mypython3/02teach_auto_test/11unittest/APITestPro/test_cases'

# 相对路径，动态获取当前文件地址
# realpath会自动判断当前系统，来取路径：windows \\  unix /
curPath = os.path.realpath(__file__)
curDir = os.path.dirname(curPath)  # 获取父目录
casePath = os.path.join(curDir, "test_cases/sign_api")  # 拼接用例目录
# print(casePath)

# 查找全部用例，pattern是匹配规则，不传也可以
discover = unittest.defaultTestLoader.discover(start_dir=casePath, pattern='test*.py', top_level_dir=None)
# print(discover)
# 生成text结果报告
runner = unittest.TextTestRunner()
runner.run(discover)
