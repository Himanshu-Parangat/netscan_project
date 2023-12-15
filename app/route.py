from types import MethodType
from flask import  render_template
from forums import Name_Forum

# Define route setup function
def setup_routes(app):
    # landing page and authentication

    @app.route('/dashboard')
    def dashboard():
        return render_template("dashboard.html")

    # @app.route('/user/<username>')
    # def show_user(username):
    #     return render_template('dashboard.html', username=username)

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

