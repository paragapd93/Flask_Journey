from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Welcome to Home Page!</h1>"

@app.route("/failed")
def failed():
    return "<h1>Sorry! You Failed!</h1>"

@app.route("/passed")
def passed():
    return "<h1>Congratulations! You Passed!</h1>"

@app.route("/welcome/<name>/<int:marks>")
def score(name, marks):
    if marks < 30:
        #Redirect to Fail Page
        return redirect(url_for("failed"))
    else:
        #Redirect to pass page
        return redirect(url_for("passed"))

    return f"<h1>Welcome {name} to our new page!</h1>"


if __name__ == "__main__":
    app.run(debug=True)
