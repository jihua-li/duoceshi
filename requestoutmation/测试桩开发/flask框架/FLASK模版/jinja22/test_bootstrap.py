from flask import Flask, render_template

app = Flask(__name__)
app.debug = True

@app.route('/send/')
def send():
    list = [
        {'id': 1, 'uuid': 'eec9de56-4fe5-11ea-bbf2-5254000db3ea', 'user': 'dcs', 'sign_id': 16, 'temp_id': 6, 'temp_type': 1, 'content': '【测试】795l0Pf6WM', 'status': 'sending', 'consume': 1, 'mobile': '13082431790', 'is_delete': 0},
        {'id': 2, 'uuid': '0085acc4-4fe6-11ea-bbf2-5254000db3ea', 'user': 'dcs', 'sign_id': 16, 'temp_id': 6, 'temp_type': 1, 'content': '【测试】795l0Pf6WM', 'status': 'sending', 'consume': 1, 'mobile': '17087829510', 'is_delete': 0},
        {'id': 3, 'uuid': '3ce7a73a-4fe6-11ea-bbf2-5254000db3ea', 'user': 'dcs', 'sign_id': 16, 'temp_id': 6, 'temp_type': 1, 'content': '【测试】795l0Pf6WM', 'status': 'sending', 'consume': 1, 'mobile': '15605783694', 'is_delete': 0},
        {'id': 4, 'uuid': 'acd414de-4fe6-11ea-bbf2-5254000db3ea', 'user': 'dcs', 'sign_id': 16, 'temp_id': 6, 'temp_type': 1, 'content': '【测试】795l0Pf6WM', 'status': 'sending', 'consume': 1, 'mobile': '14672690345', 'is_delete': 0},
        {'id': 5, 'uuid': '25822632-4fe7-11ea-bbf2-5254000db3ea', 'user': 'dcs', 'sign_id': 16, 'temp_id': 6, 'temp_type': 1, 'content': '【测试】795l0Pf6WM', 'status': 'sending', 'consume': 1, 'mobile': '13209561783', 'is_delete': 0}
    ]
    return render_template('test_bootstrap.html', result=list)

if __name__ =='__main__':
    app.run()