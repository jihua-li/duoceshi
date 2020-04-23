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


@app.route('/signlist')
def sign_list():
    logging.info("[get参数]: {}".format(request.args))
    sign_id = request.args.get("id")
    table_type = "签名列表"
    if sign_id:
        try:
            rows = db.query("select * from sms_sign where is_delete=0 and sign_id={};".format(sign_id))
        except:
            rows = db.query("select * from sms_sign where is_delete=0 order by sign_id desc limit 10;")
    else:
        rows = db.query("select * from sms_sign where is_delete=0 order by sign_id desc limit 10;")
    table_html = rows.export("html")
    table_html = table_html.replace("<table>", "<table class=\"table table-condensed\" style=\"word-break:break-all; word-wrap:break-all;\">")
    # table_html = table_html.replace("<tr>", "<tr class=\"info\" style=\"word-break:break-all; word-wrap:break-all;>\">")
    # 表示使用字符串，消除转义
    table_html = unescape(table_html)
    return render_template("test_jinja2_modify.html", table_html=table_html, table_type=table_type)


@app.route('/sendlist')
def send_list():
    table_type = "发送列表"
    rows = db.query("select * from sms_send where is_delete=0 order by id desc limit 10;")
    logging.info("[rows]: {}".format(rows.as_dict()))
    table_html = rows.export("html")
    table_html = table_html.replace("<table>", "<table class=\"table table-condensed\" style=\"word-break:break-all; word-wrap:break-all;\">")
    # table_html = table_html.replace("<tr>", "<tr class=\"info\">")
    table_html = unescape(table_html)
    return render_template("test_jinja2_modify2.html", table_html=table_html, table_type=table_type)


if __name__ == '__main__':
    app.run(debug=True, port=5003)