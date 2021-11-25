from flask import Flask,render_template
import time
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello W 打啊打大大多的大大大大   orld!'

@app.route('/1/')
def hello_world2():
    a = time.time()
    return render_template('index.html',var = a)
@app.route('/welcome/<name>')
def welcome(name):
    return 'Hello %s' % name


@app.route('/welcome/<int:id>')
def welcome2(id):
    return 'Hello id: %d' % id


if __name__ == '__main__':
    app.run()
