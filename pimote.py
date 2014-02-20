from flask import Flask
from flask import render_template

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/api/<resource>')
def api(resource = None):
    return "api says hi"

if __name__ == '__main__':
    app.run()