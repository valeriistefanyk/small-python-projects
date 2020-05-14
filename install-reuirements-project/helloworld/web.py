from helloworld.core import get_message
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html',
        message=get_message())

def run_server():
    app.run()