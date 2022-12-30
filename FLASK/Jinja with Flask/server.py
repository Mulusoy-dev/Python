from flask import Flask, render_template
import requests


app = Flask(__name__)



@app.route('/')
def hello_world():                                                               
    return render_template("index.html")


@app.route("/guess/<name>")
def guess(name):
    gender_url = f"https://api.genderize.io?name={name}"
    response1 = requests.get(gender_url)

    age_url = f"https://api.agify.io/?name={name}"
    response2 = requests.get(age_url)

    gender=response1.json()['gender']
    age=response2.json()["age"]

    return render_template('guess.html', person_name=name, gender=gender, age=age)



@app.route("/blog/<num>")
def get_blog(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    blog_data = response.json()

    return render_template('blog.html', posts=blog_data)



if __name__=="__main__":
    app.run(debug=True)

