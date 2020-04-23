import xlrd, ddt,unittest,os
from tsms_project.commons.read_excel import ExcelUtil

# 获取父路径
curPath = os.path.dirname(os.path.realpath(__file__))
#获取测试数据的绝对路径
filepath = curPath + 'test_data/data.xlsx'
sheetname = 'sheet1'
#获取测试文件中的数据
test_data = ExcelUtil(filepath,sheetname).dict_data()
print(test_data)

@ddt.ddt
class TestDdt(unittest.TestCase):
    @ddt.data(*test_data)
    def test01(self):
        pass




import re
from tsms_base import Tsmstest


def ddt_random(text, key="random"):
    ts = Tsmstest()
    data = re.sub(r'\${%s}' % key, ts.gen_ranstr(4, 4), text)
    return data


def ddt_random_all(ff, *args):
    a = ''
    print(len(args))
    for i in range(len(args)):
        if i == 0:
            a = ddt_random(ff, args[0])
        a = ddt_random(a, args[i])
    return a


if __name__ == '__main__':
    a = '''{"name": "${name}", "template": "${template}", "type": 1, "description": "${description}", "sign_id": 1}'''
    # 新需求
    b = ddt_random(a, "name")
    c = ddt_random(b, "template")
    d = ddt_random(c, "description")
    # print(b)
    # print(c)
    # print(d)
    a = ddt_random_all(a, "name")
    print(a)