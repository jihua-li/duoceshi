#面向过程：吃（猫，鱼）
#面向对象：猫.吃（鱼）
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('姓名:{}, 分数：{}' .format(self.name, self.score))

st = Student('duoceshi','99')
# st.print_score()


#私有变量，只能内部调用，防止外部调用和篡改
#如果想要外部调用私有方法，需要分装方法来调用

#练习，把age属性隐藏起来，用一个get方法，和一个set方法来代替
class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    #获取私有变量
    def get_age(self):
        return self.__age

    #修改私有变量
    def set_age(self, a):
        if 0< int(a) <=120:
            self.__age = a
        else:
            raise ValueError('invalid score para')

stu = Student('hehe', 80)
print(stu.name)
# print(stu.__age) #无法调用私有变量
print(stu.get_age())
stu.set_age(120)
print(stu.get_age())


#类的继承
#子类继承父类
#子类重写父类方法
#定义一个类，实际上就是定义了一种数据类型


#多态 ，继承父类，对父类方法进行重写

#鸭子类型
class Iterator_cls(object):
    pass


# 面向对象的三大特性
# 1.封装
# 2.继承
# 3.多态

#类中的三种方法
# 实例方法  -调用类里面的方法需要先实例化，f = Foo()  f.instance_methed()
# 静态方法 - @staticmethed 装饰器，不需要实例化，可以直接调用Foo.instance_methed()
# 类方法   - @classmethed  装饰器，不需要实例化，可以直接调用Foo.instance_methed()

