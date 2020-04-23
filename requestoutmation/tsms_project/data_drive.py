import xlrd, ddt,unittest,os,json,re
from tsms_project.commons.read_excel import ExcelUtil
from tsms_project.commons.tsms_base import Tsmstest


# 获取父路径
curPath = os.path.dirname(os.path.realpath(__file__))
#获取测试数据的绝对路径
filepath = curPath + '/test_data/data.xlsx'
print(filepath)
sheetname = 'sheet1'
#获取测试文件中的数据
test_data = ExcelUtil(filepath,sheetname).dict_data()
# print(test_data)


@ddt.ddt
class TestDdt(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.ts = Tsmstest()

    @ddt.data(*test_data)
    def test01(self, d):
        #获取参数
        data = d['data']
        #正则匹配到template的值，并进行随机替换
        data1 = re.sub(r'"\${random}', self.ts.gen_ranstr(4, 4), data, re.S)
        # print(data,type(data))
        user = d['user']
        passwd = d['passwd']
        #获取预期状态码status
        exp_status = d['status']
        #获取预期返回内容text
        exp_text =d["text"]
        # print(exp_text)
        # print(type(json.loads(exp_text)))

        #正则匹配到template值，并判断有无变量表示&{}，如果有则进行随机替换，如果没有则不替换
        # template = re.findall(r'"template": "(.*?)".*?', data)
        # template = re.findall(r'.*?"template": "(.*?)".*?', data)
        # print(template, type(template))
        # if '${}' in template[0]:
        #     data1 = re.sub(r'"template": "(.*?)".*?', self.ts.gen_ranstr(4, 4), data, re.S)
        # else:
        #     data1 = data


        # 进行创建模版操作,获取实际结果
        self.ts.req_post('temp', data1)
        self.assertEqual(exp_status, str(self.ts.status_code))
        self.assertEqual(json.loads(exp_text), self.ts.json)
        # print(type(self.ts.json))
        # print(json.dumps(self.ts.json),type(json.dumps(self.ts.json)))



if __name__ =='__main__':
    unittest.main()