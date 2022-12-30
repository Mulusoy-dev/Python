from flask import Flask, render_template
import requests


app = Flask(__name__)



@app.route('/')
def hello_world():                                                               
    return '<h1 style="text-align: center">Hello, World!</h1>'


@app.route("/guess/<name>")
def guess(name):
    gender_url = f"https://api.genderize.io?name={name}"
    response1 = requests.get(gender_url)

    age_url = f"https://api.agify.io/?name={name}"
    response2 = requests.get(age_url)
    

    gender=response1.json()['gender']
    age=response2.json()["age"]
    
    return render_template('index.html', person_name=name, gender=gender, age=age)


if __name__=="__main__":
    app.run(debug=True)

