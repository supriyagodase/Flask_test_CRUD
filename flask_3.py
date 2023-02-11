"""
Note-
If you rename a file name as either 'main4.py' or 'wsgi.py'
you can directly use 'flask run'

WSGI = Web Server Gateway Interface
Is a simple calling convention for web servers to forward requests to
web applications or frameworks written in the Python programming language.

"""

"""
"String" = (default) accepts any text without slash
"int" = accepts positive integers
"float" = accepts positive floating point values
"path" = like "string" but also accepts slashes
"uuid" = accepts UUID strings
"""

from flask import Flask,url_for

app = Flask(__name__)  # this is instance of that class


@app.route("/")  # it is decorator to tell Flask what URL should trigger our function
def hello():  # route() decorate to bind a function to a URL
    return "<h1> hello supriya </h1>"


# <converter:variable_name>
@app.route("/addition/<int:num1>/<int:num2>")
def add(num1, num2):
    result = num1 + num2
    return f"<h1>{result}</h1>"


@app.route("/about/<institute>")
def about(institute):
    print(type(institute))
    return f"<h1> Handcrafted by Supriya - {institute}</h1>"


@app.route("/")
def index():
    return "Index Page"


if __name__ == "__main__":
    print(url_for('about'))

    app.run(host="localhost", port=8080)
    print(url_for('about'))

