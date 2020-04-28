"http://table.finance.yahoo.com/table.csv?s=000001.sz"


# 下载内容到文件urllib.urlretrieve
from urllib.request import urlretrieve

# 将指定内容下载文件中
urlretrieve('http://table.finance.yahoo.com/table.csv?s=000001.sz', './pingan.csv')

import csv

with open('pingan.csv', 'rb') as rf:
    reader = csv.reader(rf)
    with open('pingan2.csv', 'wb') as wf:
        writer = csv.writer(wf)
        headers = reader.next()  # 读取首行数据
        writer.writerow(headers)
        for row in reader:
            if row[0] > '2016-01-01':
                break
            if int(row[5] > 5000000):
                writer.writerow(row)

print('end')