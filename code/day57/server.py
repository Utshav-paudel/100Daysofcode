from flask import Flask, render_template
import random
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    current_date = datetime.date.today().year
    random_num = random.randint(1,10)
    return render_template("index.html", num=random_num , cur_date=current_date)

if __name__ == "__main__":
    app.run(debug=True)



