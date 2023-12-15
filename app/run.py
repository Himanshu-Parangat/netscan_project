from flask import Flask, render_template

# Create a Flask application
app = Flask(__name__)


# landing page and aurthintication 
@app.route('/')
def index():
    return render_template("index.html")


# @app.route('/user/<username>')
# def show_user(username):
#     # Assuming you have a templates folder with a file named 'user.html'
#     return render_template('dashboard.html', username=username)


# landing page and aurthintication 
@app.route('/dashboard')
def dashboard():
    return render_template("dashboard.html")


# Run the Flask app if this script is the main program
if __name__ == '__main__':
    app.run()

