import json
from flask import Flask, request

app = Flask(__name__)

class MyDB:
    """
    class that is runtime DB.
    Note - this DB persists data as long as app is running
    """
    foo = []

@app.get("/data")
def get_data():
    """
    HTTP GET request from postman/browser
    :return: HTML data string
    """
    return f'<h1> data aviable - {MyDB.foo}</h1>'

@app.post("/data")
def post_data():
    breakpoint()
    return '<h1>.....</h1>'