from flask import Flask
from markupsafe import escape

app = Flask(__name__)
#creating decorators
def make_bold(function):
    def wrapper():
        return "<b>" + function() +"</b>"
    return wrapper
def make_emphasis(function):
    def wrapper():
        return "<em>" + function() +"</em>"
    return wrapper
def make_underline(function):
    def wrapper():
        return "<u>"+function()+"</u>"
    return wrapper
@app.route("/")
def hello_world():
    return "<p>Hello, World!"\
        "</p><p>This is a pragraph</p>"\
        "<img src='',alt='image'>"
# working with flask url
@app.route("/<name>/<int:number>")
def greet(name, number):
    return (f"Hello {name}! You are {number} years old")

# using decorator we created
@app.route("/bye")
@make_bold
@make_emphasis
@make_underline
def bye():
    return "Bye"
# advanced python decorator functions
class User:
    def __init__(self,name):
        self.name = name
        self.is_logged_in = False
def create_blog_post(user):
    print(f"This is {user.name}'s new blog post.")
new_user = User("utshav")
if __name__ == "__main__":
    app.run(debug=True)