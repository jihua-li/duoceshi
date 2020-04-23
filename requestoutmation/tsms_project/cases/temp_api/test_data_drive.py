import xlrd, ddt,unittest,os
from tsms_project.commons.read_excel import ExcelUtil

# 获取父路径
curPath = os.path.dirname(os.path.realpath(__file__))
#获取测试数据的绝对路径
filepath = curPath + 'test_data/data.xlsx'
print(filepath)
sheetname = 'sheet1'
#获取测试文件中的数据
# test_data = ExcelUtil(filepath,sheetname).dict_data()
# print(test_data)

@ddt.ddt
class TestDdt(unittest.TestCase):
    @ddt.data(*test_data)
    def test01(self):
        pass