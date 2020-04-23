from flask import Flask, render_template, request
import records
from db_config import *
import logging
from xml.sax.saxutils import unescape
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)-16s %(levelname)-8s %(message)s')

db = records.Database(
    'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(
        config.get("user"),
        config.get("passwd"),
        config.get("host"),
        config.get("port"),
        config.get("db"),
    )
)


app = Flask(__name__)
app.debug = True

@app.route('/signlist/<length>/')
def sign_list(length):
    table_type = "签名列表"
    #可接收args参数sign_id=
    signid = request.args.get('sign_id')
    logging.info('获取请求的sign_id为：{}'.format(signid))
    if signid:
        rows = db.query("select * from sms_sign where sign_id={} and is_delete=0 order by sign_id desc limit {};".format(signid,length))
    else:
        rows = db.query("select * from sms_sign where is_delete=0 order by sign_id desc limit {};".format(length))
    #将数据查询的结果处理成html
    table_html = rows.export("html")
    #records处理成的html没有任何样式，需要添加样式
    table_html = table_html.replace("<table>", "<table class=\"table table-condensed\" style=\"word-break:break-all; word-wrap:break-all;\">")
    table_html = table_html.replace("<tr>", "<tr class=\"info\" style=\"word-break:break-all; word-wrap:break-all;>\">")
    table_html = unescape(table_html)
    return render_template("test_jinja2_modify.html", table_html=table_html, table_type=table_type, len=length)


@app.route('/sendlist')
def send_list():
    table_type = "发送列表"
    rows = db.query("select * from sms_send where is_delete=0 order by id desc limit 10;")
    logging.info("[rows]: {}".format(rows.as_dict()))
    # 将数据查询的结果处理成html
    table_html = rows.export("html")

    table_html = table_html.replace("<table>", "<table class=\"table table-condensed\" style=\"word-break:break-all; word-wrap:break-all;\">")
    table_html = table_html.replace("<tr>", "<tr class=\"info\">")
    table_html = unescape(table_html)
    return render_template("test_jinja2_modify.html", table_html=table_html, table_type=table_type)


if __name__ == '__main__':
    app.run(port=5003)