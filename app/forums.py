from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired, ValidationError



class Name_Forum(FlaskForm):
    def validate_name(self, field):
        if not field.data.isalpha():
            raise ValidationError('Invalid Credentials')

    name = StringField("What's your name", validators=[DataRequired(), validate_name])
    password = PasswordField("Enter your password", validators=[DataRequired()])
    submit = SubmitField("Submit")

