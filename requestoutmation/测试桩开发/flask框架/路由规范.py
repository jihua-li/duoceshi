"""
定义路由的时候一定要注意规范，尽量要以 / 结尾， 如使  /rule/ ，而不是 /rule

解释说明:
1. 当两者同时使用时，各自生效。即:使 /rule访问，会路由到roule_1;使 /rule/访问会路由到 roule_2
2. 当仅使用:/rule时。使用/rule访问，会路由到roule_1;使用/rule/访问会报错404
3. 当仅使用:/rule/时。使用/rule/访问，会路由到roule_2;使用/rule访问，会重定向
到 /rule/ ，从而也访问 roule_2
所以从规范上讲，使用 / 结尾的路由，兼容性更好
"""


from flask import Flask

app = Flask(__name__)
app.debug = True

@app.route('/rule')
def rule_1():
    return 'rult1'

@app.route('/rule/')
def rule_2():
    return 'rule2'


if __name__ =='__main__':
    app.run(host='0.0.0.0', port=5001)