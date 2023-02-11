from flask import Flask, render_template

app = Flask(__name__)

cricketers = ["virat", "hardik", "rahul"]


@app.route("/cricketers/")
@app.route("/cricketers/<string:all_>")
def details(all_=None):
    return render_template(
        "dynamic_hello.html",
        all_=all_,
        cricketers=cricketers)

