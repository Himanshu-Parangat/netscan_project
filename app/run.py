from flask import Flask 
from route import setup_routes


# Create a Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = "this_will_change"

# Set up routes from route.py
setup_routes(app)

# Run the Flask app if this script is the main program
if __name__ == '__main__':
    app.run()

