from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route("/username/<name>/1")                                            # <name> str Type
def greet(name):
    return f"Welcome {name}!"


@app.route("/number/<int:number>")                                         # <int> int Type
def show_post_id(number):
    return f"number: {number}"


@app.route("/bye")
def bye():
    return "See You Again!"


if __name__ == "__main__":
    app.run(debug=True)                                                    # equal to 'flask run'

    