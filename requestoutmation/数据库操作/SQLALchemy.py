'''ORM -- relational mapping'''
from sqlalchemy import Column, String,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from tsms_project.commons.tsms_db import OperationDb
from tsms_project.commons.tsms_base import Tsmstest

# 持原生sql，又支持持ORM。安装: pip install SQLAlchemy
#ORM > Object-Relational Mapping:把关系型数据库的表结构映射到对象上，通过操作对象，来操作数据库

#创建对象基类
Base = declarative_base()
#集成基类
class Students(Base):
    __tablename__ = "students"
    id = Column(String(20), primary_key= True)
    name = Column(String(20))


# 初始化数据库连接:'数据库类型+数据库驱动名称:// 户名: 令@机 地址:端 号/数据库名'
engine = create_engine('mysql+pymysql://root:123456@192.168.0.148:3306/flaskblog?charset=utf8')
#创建DBsession
DBsession = sessionmaker(bind=engine)
#创建session对象
session = DBsession()

ts = Tsmstest()
# list_2 = []
for i in range(10):
    # list_2.append({"id":ts.gen_ranstr(3), "name":ts.gen_ranstr(0,4)})
    a = {"id":ts.gen_ranstr(3), "name":ts.gen_ranstr(0,4)}
    new_student = Students(**a)
    session.add(new_student)
session.commit()
session.close()
