from flask import Flask, render_template
import random
import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    current_date = datetime.date.today().year
    random_num = random.randint(1,10)
    return render_template("index.html", num=random_num , cur_date=current_date)

#using api to guess gender and age from name
@app.route('/guess/<name>')
def guess(name):
    gender_guess = requests.get(f"https://api.genderize.io?name={name}")
    gender_json = gender_guess.json()
    gender = gender_json["gender"]
    #age
    age_guess = requests.get(f"https://api.agify.io?name={name}")
    age_json = age_guess.json()
    age = age_json["age"]
    return render_template("guess.html",person_name=name, person_gender=gender , person_age=age)

#blog
@app.route('/blog/<num>')
def get_blog(num):
    blog_url = "https://api.npoint.io/7aa748e1f1e4d6c21d80"
    response = requests.get(blog_url)
    blog_lists = response.json()
    print(num)
    return render_template("blog.html", all_blog=blog_lists, )

if __name__ == "__main__":
    app.run(debug=True)



