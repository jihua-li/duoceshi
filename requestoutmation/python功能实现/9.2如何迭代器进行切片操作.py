from itertools import islice

# print(help(islice))

"""有某个文本文件，我们想读取其中某范围的内容，如100-200行之间的内容，python中文本文件是可以迭代的对象，
我们是否可以使用类似列表切片的方式得到一个100到200文件内容的生成器？"""

# with open('2020-02-14.log', 'r') as f:
#     # for line in islice(f, 10, 15): #截取10到15行的数据, 步进值不传则默认为1
#     for line in islice(f, 10): #截取前10行
#     # for line in islice(f, 50, None): #截取前50行到末尾

        # print(line)


l = [x for x in range(20)]
t = iter(l)
for x in islice(t, 5, 10): #对迭代器进行切片操作时数据会被消耗，但如果加t = iter(l)，直接对l进行切片取值则不会存在这个问题（这里我还不是很明白！！）
    print(x)
print('=' * 5)
for i in t:
    print(i)