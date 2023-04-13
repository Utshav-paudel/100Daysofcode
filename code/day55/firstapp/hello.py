# Import the Flask class from the flask module
from flask import Flask

# Create a new instance of the Flask class with the name of the module
app = Flask(__name__)

# Define a route for the root URL ("/") that returns a "Hello, World!" message
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

# If this script is executed directly (i.e. not imported), start the development server
if __name__ == "__main__":
    app.run()
