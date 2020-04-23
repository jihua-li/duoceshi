"""背景"""
# ASCIIMA 英文编码
# 码表网址： http://www.asciima.com/

# gbk  中文编码

# 万国码 unicode字符集  准确说是utf-16 (16代表16个位)

# utf-8 可变长编码方式


"""编码"""

#1、字符串转字节串，编码过程：字符串 -->字符集映射表 -->字节串
a = '黎记华'.encode('utf-8')
print(a, type(a))

b = '黎记华'.encode('gbk')
print(b, type(b))

c = '黎记华'.encode('unicode-escape')
print(c, type(c))

#在python中字符串转字节串的三种方法



#2、字节串转字符串，解码过程：字节串 -->字符集映射表 -->字符串