from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField
from wtforms.validators import DataRequired


class PasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Submit')


class PWGeneratorForm(FlaskForm):
    submit = SubmitField('Generate Password', validators=[DataRequired()])
