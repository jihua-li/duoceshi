import xlrd,logging,os

logging.basicConfig(level=logging.INFO, format=('%(asctime)-16s %(levelname)-8s %(message)s'))

class ExcelUtil:
    def __init__(self, filename, sheetname):
        #获取Excel内容
        self.data = xlrd.open_workbook(filename)
        #获取指定table的内容
        self.table = self.data.sheet_by_name(sheetname)
        #获取首行的内容作为key值，为list
        self.keys = self.table.row_values(0)
        #获取总行数
        self.rownum = self.table.nrows
        #获取总列数
        self.colnum = self.table.ncols

    def dict_data(self):
        if self.rownum <= 1:
            logging.info('[总行数小于1，请检查数据是否正确]')
        else:
            r = []
            j = 1
            for i in range(self.rownum-1):
                s = {}
                values = self.table.row_values(j)
                for c in range(self.colnum):
                    s[self.keys[c]] = values[c]
                r.append(s)
                j +=1
            return r


if __name__ =='__main__':
    filepath = '/Users/lijihua/PycharmProjects/duoceshi/requestoutmation/tsms_project/test_data/data.xlsx'
    sheetname = 'sheet1'
    # eu = ExcelUtil(filepath, sheetname)
    # print(eu.dict_data())

root_dir = os.path.abspath(os.path.join(os.getcwd(),"../.."))
# root_dir = os.path.abspath(r"../..")
print(root_dir)