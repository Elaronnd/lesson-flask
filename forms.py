from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Email, DataRequired


class UserForm(FlaskForm):
    username = StringField("Введіть username", validators=[DataRequired()])
    email = StringField("Введіть email", validators=[DataRequired()])
    submit = SubmitField("Submit")
