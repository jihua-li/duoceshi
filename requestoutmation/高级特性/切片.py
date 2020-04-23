#list,tuple,str都支持切片，只是tuple切片还是tuple,str切片还是str
a = 'hellokitty'
# 指定范围，从1开始，到4结束，但是不取最后1个
print(a[1:4])
# 从头开始
print(a[:4])
# 倒数切片，去掉最后一个
print(a[:-1])
#取后5个
print(a[-5:])
# 从0取到5，每2个取1个
print(a[:5:2])
print(a[0:5:2])
# 从头取到最后，每5个取1个
print(a[::5])
print(a[0::5])
# 倒顺序, 反转
print(a[::-1])