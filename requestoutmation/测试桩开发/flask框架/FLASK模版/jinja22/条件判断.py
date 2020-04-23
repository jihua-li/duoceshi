from flask import Flask, render_template

app = Flask(__name__)
app.debug = True

@app.route('/score/<int:score>/')
def student(score):
    return render_template('score.html', score=score)

if __name__ =='__main__':
    app.run()