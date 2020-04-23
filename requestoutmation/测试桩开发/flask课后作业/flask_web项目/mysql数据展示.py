from flask import Flask, render_template
import logging, records

app = Flask(__name__)
app.debug = True


#连接数据库
def connect_db(sql):
    db = records.Database('mysql+pymysql://root:dcs123@148.70.194.135:3306/flaskblog?charset=utf8')
    res = db.query(sql)
    return res


@app.route('/sign/')
def show_sign():
    #查询数据库数据
    sql = 'SELECT createtime,sign_id,pics,audit_status FROM `sms_sign` ORDER BY createtime desc;'
    res = connect_db(sql)
    #将数据查出来的结果转换成list，再将list中的值转换成dict, 并以list的格式输出
    res_list = list(map(dict, list(res)))
    #将数据库查到的数据以list的形式传给html文档遍历取值
    return render_template('get_sign.html', result=res_list)

if __name__ =='__main__':
    app.run()


# sql = 'SELECT createtime,sign_id,pics,audit_status FROM `sms_sign` limit 1;'
# res = connect_db(sql)
# res_list = list(map(dict, list(res)))
# for r in res_list:
#     for k, v in r.items():
#         print(v)
#
#
# print(res_list)
