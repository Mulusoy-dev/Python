from flask import Flask, render_template
import requests

app = Flask(__name__)



@app.route('/')
def home():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    blog_data = response.json()

    return render_template('index.html', posts=blog_data)


@app.route('/post/<int:num>')
def post(num):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    blog_data = response.json()
    print(blog_data[num-1])
    
    return render_template('post.html', post=blog_data[num-1])
    




if __name__ == "__main__":
    app.run(debug=True)
