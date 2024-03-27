from flask import Flask, request, make_response, redirect, render_template, session
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config["SECRET_KEY"] = "CLAVE SEGURA"


@app.route("/index")
def index():
    user_ip_information = request.remote_addr
    response = make_response(redirect("/show_information_address"))
    session["user_ip_information"] = user_ip_information
    return response


items = [
    "ITEM 1",
    "ITEM 2",
    "ITEM 3",
    "ITEM 4",
]


class LoginForm(FlaskForm):
    username = StringField("Nombre del usuario", validators=[DataRequired()])
    password = PasswordField("contraseña", validators=[DataRequired()])
    submit = SubmitField("Enviar datos", validators=[DataRequired()])


@app.errorhandler(404)
def not_found_endpoint(error):
    return render_template("404.html", error=error)


@app.route("/show_information_address", methods=["GET", "POST"])
def show_information():
    user_ip = session.get("user_ip_information")
    username = session.get("username")
    login_form = LoginForm()
    context = {
        "user_ip": user_ip,
        "items": items,
        "login_form": login_form,
        "username": username,
    }
    if login_form.validate_on_submit():
        username = login_form.username.data
        session["username"] = username
        return make_response(redirect("/index"))

    return render_template("ip_information.html", **context)


app.run(host="0.0.0.0", port=5000, debug=True)
