from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Welcome to Home Page!</h1>"


@app.route("/welcome/<name>")
def welcome(name):
    return f"<h1>Welcome {name} to our new page!</h1>"


if __name__ == "__main__":
    app.run(debug=True)
