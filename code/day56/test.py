class User:
    def __init__(self,name):
        self.name = name
        self.is_logged_in = False


# created decorate to authenicate
def is_authenicate_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].is_logged_in == True:
            function(args[0])
    return wrapper
@is_authenicate_decorator
def create_blog_post(user):
    print(f"This is {user.name}'s blog post.")

new_user = User("utshav")
new_user.is_logged_in = True
create_blog_post(new_user)