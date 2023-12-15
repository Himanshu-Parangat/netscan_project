from flask import Flask 
from route import setup_routes
from flask import render_template

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators
from wtforms.validators import DataRequired, ValidationError


# Create a Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = "this_will_change"


class Name_Forum(FlaskForm):
    def validate_name(self, field):
        if not field.data.isalpha():
            raise ValidationError('Invalid Credentials')

    name = StringField("What's your name", validators=[DataRequired(), validate_name])
    password = PasswordField("Enter your password", validators=[DataRequired()])
    submit = SubmitField("Submit")



@app.route('/', methods=['GET','POST'])
def index():
    name = None
    form = Name_Forum()

    # validate input
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''

    return render_template("index.html",
                           name = name,
                           form = form)


# Set up routes from route.py
setup_routes(app)

# Run the Flask app if this script is the main program
if __name__ == '__main__':
    app.run()

