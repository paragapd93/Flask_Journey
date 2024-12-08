from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Welcome to Home Page!</h1>"

@app.route("/failed/<sname>/<int:marks>")
def failed(sname, marks):
    return f"<h1>Sorry {sname}! You Failed with {marks} marks!</h1>"

@app.route("/passed/<sname>/<int:marks>")
def passed(sname, marks):
    return f"<h1>Congratulations {sname}! You Passed with {marks} marks!</h1>"

@app.route("/welcome/<name>/<int:marks>")
def score(name, marks):
    if marks < 30:
        #Redirect to Fail Page
        return redirect(url_for("failed",sname=name, marks=marks))
    else:
        #Redirect to pass page
        return redirect(url_for("passed",sname=name, marks=marks))

    return f"<h1>Welcome {name} to our new page!</h1>"


if __name__ == "__main__":
    app.run(debug=True)
