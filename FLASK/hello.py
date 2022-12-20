from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route("/username/<name>")                                            # <name> str Type
def greet(name):
    return f"Welcome {name}!"


@app.route("/<name>/<int:number>")                                         # <int> int Type
def info(name, number):
    return f"Hello {name} you are {number} years old."


@app.route("/bye")
def bye():
    return "See You Again!"


if __name__ == "__main__":
    app.run(debug=True)                                                    # equal to 'flask run'

    