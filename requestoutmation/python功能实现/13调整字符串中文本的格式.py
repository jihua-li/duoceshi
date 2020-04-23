"""将日志文件中的日期格式yyyy-mm-dd, 修改为dd/mm/yyyy
   使用正则表达式re.sub()方法做字符串替换，利用正则表达式的捕获组，捕获每个部分内容，在替换字符串中调整各个捕获组的顺序"""

import re

with open('./2020-02-14.log', 'r') as f:
    log = f.read()
    # print(log)
    #通过正则提取日期，year,month,day, 捕获每个部分内容，在替换字符串中调整各个捕获组的顺序
    #其中?P<year>的写法为获取的内容打上标签，后面获取通过\g<year>获取内容
    res = re.sub('(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})', '\g<day>/\g<month>/\g<year>', log)
    print(res)