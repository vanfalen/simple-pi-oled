from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/terminal",methods=['POST'])
def hello():
    return "Hello, %s"%(request.form["user"])
