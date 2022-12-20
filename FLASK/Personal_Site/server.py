from flask import Flask
from flask import render_template
app = Flask(__name__, template_folder='C:/Users/melih/Desktop/Python/FLASK/Personal_Site/templates')


@app.route("/")
def home():
    return render_template('index.html')





if __name__=="__main__":
    app.run(debug=True)

   