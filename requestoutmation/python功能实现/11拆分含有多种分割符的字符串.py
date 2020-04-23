"""我们要把某个字符串根据分隔符拆分不同的字段，该字符串包含多种不同的分隔符
   例如：s = 'ab;cd|efg|hi,jkl|mn\topq,uvw\txyz' """


#单一分隔符的情况
s = '501 43959 43955   0 29Mar20 ttys001    0:00.93 -bash'
s1 = s.split() #split第一个参数是分隔符，空白的就不需要传：比如空格、\t、\n等都是
print(s1)

#包含多种不同分隔符
#方法一：str.split()
s = 'ab;cd|efg|hi,jkl|mn\topq,uvw\txyz'
a = s.split(';')
print(a)

b = map(lambda x: x.split('|'), a)
print(list(b)) #是一个多元列表

t = []
# map(lambda x: t.extend(x.split('|')), a)
# for x in a:
#     t.extend(x.split('|'))
# print(t)
map(lambda x: t.extend(x.split('|')), a)
print(t)

# def ss(x, d):
#     t = []
#     t.extend(x.split(d))
#     return t

def mysplit(s, ds):
    res = [s]
    for d in ds:
        t = []
        # map(lambda x: t.extend(x.split(d)), res) #没有起作用，还没找到问题
        print(t)
        for x in res:
            t.extend(x.split(d))
        res = t
    return [x for x in res if x]

s = 'ab;cd|efg|hi,,jkl|mn\topq,uvw\txyz'
print(mysplit(s, ';|,\t'))

#方法二,使用正则表达式，re.split()，推荐*****
import re
res = re.split('[;|,\t]+', s) #第一个参数中的 + 号是表示处理多个
print(res)
