"""如何去掉字符串中不需要的字符"""

import re
import string

#第一种方法
# 去掉两边str.strip(), 去掉左边lstrip(), 去掉右边rstrip()
s = '  abc  123  '
#不传值，则默认去掉空格，\t, \r等
print(s.strip())
print(s.lstrip())
print(s.rstrip())

s1 = '---abc+++'
#去掉字符串两边的- + 号
print(s1.strip('-+'))

#方法二，删除固定位置的字符，可以使用切片 + 拼接的方法
s2 = 'abc:123'
print(s2[:3] + s2[4:])


#方法三 ：字符串的replace()方法，或正则表达式re.sub()删除任意字符串
s3 = '\tabd\t234\tefg'
print(s3.replace('\t', '')) #replace()方法只能替换一种字符


s4 = '\tabd\t234\tefg\rhig\r'
print(re.sub('[\t\r]', '', s4))



#方法四：字符串的translate()方法，可以同时删除多种不同的字符

#字符替换，比如加密

s5 = 'abc1234xyz'
#将abc和xyz对调
print(str.maketrans('abcxyz', 'xyzabc'))
print(s5.translate(str.maketrans('abcxyz', 'xyzabc')))

#将abc替换成xyz
intab = 'abc'
outab = 'xyz'
print(s5.translate(str.maketrans(intab, outab)))


s6 = '\tabc\rxyz\n234'

print(s6.translate(None, '\t\r\n')) #python3不可用