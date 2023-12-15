from flask import  render_template


# Define route setup function
def setup_routes(app):
    # landing page and authentication
    @app.route('/')
    def index():
        return render_template("index.html")

    # landing page and authentication
    @app.route('/dashboard')
    def dashboard():
        return render_template("dashboard.html")

    # @app.route('/user/<username>')
    # def show_user(username):
    #     return render_template('dashboard.html', username=username)
