from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField("Nombre del usuario", validators=[DataRequired()])
    password = PasswordField("contraseña", validators=[DataRequired()])
    submit = SubmitField("Enviar datos")
