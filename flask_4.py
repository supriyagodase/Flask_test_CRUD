"""
MVC => (Model - View - Control)

MVT => (Model -templates - View)
In terms of flask

Model - 'data_models'
View - 'templates'
Control - 'saving_account','current_account'

Model => Database related part(data structure,DDl)

HTML - Building Web page
css- styling
"""

from flask import Flask, render_template
import flask_3

app = Flask(__name__)


@app.route("/hello")
def hello():
    """
    this is a we access the html file in the flask..i.e fetch the data
    :return:
    """
    return render_template("hello.html")