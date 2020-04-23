from flask import Flask, redirect, render_template, request, flash
import logging
from test_tsms_project_pytest_pansir.tsms_pytest_commons.tsms_rds import TsmsRedis

logging.basicConfig(level=logging.INFO, format='%(asctime)-16s %(levelname)-8s %(message)s')

app = Flask(__name__)
app.secret_key = "super secret key"

rds = TsmsRedis()


@app.route("/money/", methods=["GET", "POST"])
def sub_money():
    if request.method == "GET":
        return render_template("test_modify_redis.html")
    elif request.method == "POST":
        req_data = request.form
        user = req_data.get("user")
        money = req_data.get("money")
        if not money:
            flash("提交金额为空，请输入金额！！！")
            return render_template("test_modify_redis.html")
        try:
            int(money)
        except Exception as e:
            flash("修改失败，提交金额不为整数！！！")
            return render_template("test_modify_redis.html")
        try:
            now_money = rds.get_account(user)
            logging.info("[now_money is]: {}".format(now_money))
        except Exception as e:
            logging.error("[用户余额查询失败]")
            logging.error(e)
            flash("用户余额查询失败，账户不存在！！！")
            return render_template("test_modify_redis.html")
        try:
            rds.set_account(user=user, value=money)
        except Exception as e:
            logging.error("[设置金额失败]: {}".format(e))
            flash("设置金额失败")
            return render_template("test_modify_redis.html")
        flash("设置成功!")
        return render_template("test_modify_redis.html")


if __name__ == '__main__':
    # app.secret_key = 'super secret key'
    # app.config['SESSION_TYPE'] = 'filesystem'
    app.run(port=5004, debug=True)