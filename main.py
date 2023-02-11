"""
How to run flask application?

```
flask --app main run
```

"""

from flask import Flask

app1 = Flask(__name__)


@app1.route("/")
def hello_world():
    return "<p> hello world!!</p>"


if __name__ == '__main__':
    app1.run()
