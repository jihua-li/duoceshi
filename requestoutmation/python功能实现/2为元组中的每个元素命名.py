"""为元组中的每个元素命名，提高程序可读性"""

#方法一
#定义类似与其他语言的枚举类型，也就是定义一系列的数值常量
student = ('Jim', 16, 'male', 'jim555@qq.com')

name, age, sex, email = range(4)

print(student[name])

#方法二
#使用标准库中collections.namedtuple替代内置tuple
from collections import namedtuple

students = namedtuple('student', ['name', 'age', 'sex', 'email'])

s = students('Jim', 16, 'male', 'jim555@qq.com')
print(s)

s2 = students(name='Jim', age=16, sex='male', email='jim555@qq.com')
print(s2)

#通过变量名获取元组的值
print(s.name)
print(s.age)
print(s.sex)
print(s.email)


#查看s是不是内置类型的tuple, True 就说说明普通元组能用的地方就能使用如s.name
print(isinstance(s, tuple))