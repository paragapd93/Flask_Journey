from flask import (Flask,
                   redirect,
                   render_template,
                   url_for,
                   flash)
from forms import SignupForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'this_is_CSRF_token'

@app.route("/")
def home():
    return render_template("home.html", title="Home")

@app.route("/login", methods = ['GET','POST'])
def login():
    form = LoginForm()
    email = form.email.data
    pwd = form.password.data
    if form.validate_on_submit():
        if email == 'abc@d.com' and pwd == '12345678':
            flash("logged In Successfully!")
            return redirect(url_for("home"))
        else:
            flash("Incorrect Credentials!")
    return render_template("login.html", title="Login", form=form)

@app.route("/signup", methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        flash(f"Successfully Registered {form.username.data}")
        return redirect((url_for("home")))
    return render_template("signup.html", title="Signup", form=form)

if __name__ =="__main__":
    app.run(debug=True)