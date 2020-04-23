import xlrd,logging

logging.basicConfig(level=logging.INFO, format=('%(asctime)-16s %(levelname)-8s %(message)s'))

class ExcelUtil():
    def __init__(self, excelPath, sheetName):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(sheetName)
        # 获取第一行作为key值,为一个列表
        self.keys = self.table.row_values(0)
        # 获取总行数
        self.rowNum = self.table.nrows
        # 获取总列数
        self.colNum = self.table.ncols

    def dict_data(self):
        if self.rowNum <= 1:
            # print("总行数小于1")
            logging.error("总行数小于1")
        else:
            r = []
            j = 1
            for i in range(self.rowNum - 1):
                s = {}
                # 从第二行取对应的values值
                values = self.table.row_values(j)
                for x in range(self.colNum):
                    # logging.info('x={}'.format(x))
                    s[self.keys[x]] = values[x]
                r.append(s)
                j += 1
            return r


if __name__ == '__main__':
    # filePath = '/Users/lijihua/PycharmProjects/duoceshi/requestoutmation/tsms_project/test_data/data.xlsx'
    filePath = '/Users/lijihua/PycharmProjects/duoceshi/requestoutmation/tsms_project/test_data/data.xlsx'
    sheetName = 'sheet1'
    data = ExcelUtil(filePath, sheetName)
    print(data.dict_data())
