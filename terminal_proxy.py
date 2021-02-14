from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/terminal",methods=['POST','GET'])
def hello():
    try:
        from oled_terminal import oled_term
        from time import sleep
        myTerm=oled_term()
        myTerm.print_line("Hello %s"%(request.form["user"]))
        sleep(10)
    except Exception as e:
        return str(e)
    return "Hello, %s"%("Emmanuel")

if __name__ == '__main__':
    app.run(debug=True)

