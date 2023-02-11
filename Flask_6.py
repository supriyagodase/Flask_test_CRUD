from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route("/manager")
def greet_manager():
    url = url_for("greet_employee", name="supriya")
    print(url)
    return "<h1> Manager:: Good Morning </h1>"


@app.route("/employee/<name>")
def employee(name):
    return f"<h1> Good mor {name} </h1>"


@app.route("/client/<client>")
def greet_client(client):
    return f"<h1> Good mor {client} </h1>"


@app.route("/user/<use_type>/<name>")
def greet_everyone(use_type, name_):
    if use_type == "employee":
        emp_url = url_for("greet_employee", name=name_)
        return redirect(emp_url)
    elif use_type == "client":
        client_url = url_for("greet client", client=name_)
        return redirect(client_url)
    return f"<h1> choose either employee or client </h1>"


if __name__ == "__main__":
    app.run(debug=True)
    url = url_for("employee", name="supriya")
    print(url)
