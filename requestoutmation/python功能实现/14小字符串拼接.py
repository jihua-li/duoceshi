"""将多个小字符串拼接成一个大字符串"""

#普通的拼接, 直接使用 + 号
s1 = 'abcd'
s2 = 'efgh'
s3 = s1 + s2
print(s3)

#使用str.join()方法进行拼接
l1 = ['ab', 'cd', 'ef']
#以；号进行拼接
s5 = ';'.join(l1)
print(s5)
#以空格进行拼接
s6 = ''.join(l1)
print(s6)

#如果拼接中包含数字处理方法
l2 = ['ab', 12, 34, 'cd']
# s7 = ''.join(l2) #直接拼接会报错
# print(s7)
#正确方法
s8 = ''.join(str(x) for x in l2)
s9 = ''.join([str(x) for x in l2])
print(s8)
print(s9)
