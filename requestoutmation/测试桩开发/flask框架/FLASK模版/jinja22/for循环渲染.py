from flask import Flask, render_template

app = Flask(__name__)
app.debug = True

@app.route('/students/')
def result():
    dict = {
        'ld': 90,
        'scl': 90,
        'ljh': 90,
        'qxl': 90,
        'xp': 90,
        'hhc': 90,
        'wjq': 90,
    }
    return render_template('students.html', result=dict)

if __name__ =='__main__':
    app.run()