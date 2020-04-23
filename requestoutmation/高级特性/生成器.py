'''generator'''
#解决数据量大时内存溢出的问题,和列表生成式的区别就是把【】换成了（）
b = (x * x for x in range(1000000000))
# print(b)

#使用yield返回，函数的本质会发生改变，变成了生成器，能够迭代的关键是他有next()方法



'''yield实战'''
import time
'''实时监控日志'''

def tail(f):
    # 第一个参数：偏移量
    # 第二个参数：0，代表文件开始，1，代表文件当前位置，2，代表文件末尾
    f.seek(0, 2)  # 移动到文件最后一行
    while True:
        line = f.readline()  # 读取文件中新的文本行
        if not line:
            # 没有最新行，则每0.1秒执行一次
            time.sleep(0.1)
            # print("wait wait")
            continue
        yield line


# tail -f info.log |grep python
def grep(lines, searchtext):
    # 遍历lines生成器
    for line in lines:
        # 判断是否包含关键字
        if searchtext in line:
            # 若包含则返回
            yield line


# 模拟tail -f |grep python
# 获取生成器
flog = tail(open('test.log'))
# 把生成器当作可迭代对象传入，继续yield返回，pylines得到的也是一个生成器
pylines = grep(flog, 'python')
# 再次遍历生成器，将返回结果打印
for line in pylines:
    print(line, )