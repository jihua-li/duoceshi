
#方法一，使用str.ljust()左对齐，str.rjust()右对齐，str.center()
a = 'abc'

#左对齐
la1 = a.ljust(20) #以20个空格向左对齐
print(len(la1), la1)
la2 = a.ljust(20, '=') #以20个=向左对齐
print(la2)

#右对齐
ra1 = a.rjust(20)
print(ra1)
ra2 = a.rjust(20, '=')
print(ra2)


#方法二， format()方法
#左对齐
print('左对齐：', format(a, '<20'))
#右对齐
print('右对齐：', format(a, '>20'))
#居中
print('居中：', format(a, '^20'))

d = {
    'skjfjall': 'sjf',
    'ajsdkfjlajsdfj': 'df',
    'dsf': 'df',
    'skjf': 4,
    'sdjfsdj': 'sgssdfsf'
}

max_key = max(map(len, d.keys()))
print(max_key)

new_d = {}
#居中对齐
for k in d:
    new_d[k.ljust(max_key)] =d[k]
    print(k.ljust(max_key), ':', d[k])

print(new_d)