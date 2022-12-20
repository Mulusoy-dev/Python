from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():                                                               # HTML and CSS redering in Flask 
    return '<h1 style="text-align: center">Hello, World!</h1>' \
            '<p>This is Paragraph</p>' \
            '<img src="https://media.giphy.com/media/4VglqgTazN7YQ/giphy.gif" width=300>'                            
            



@app.route("/username/<name>")                                            # <name> str Type
def greet(name):
    return f"Welcome {name}!"


@app.route("/<name>/<int:number>")                                         # <int> int Type
def info(name, number):
    return f"Hello {name} you are {number} years old."

# Decorator Definitions

def make_bold(function):
    result = function()
    def wrap_function():
        return f"<b>{result}</b>"
    return wrap_function



def make_emphasis(function):
    result = function()
    def wrap_function():
        return f"<em>{result}</em>"
    return wrap_function



def make_underlined(function):
    result = function()
    def wrap_function():
        return f"<u>{result}</u>"
    return wrap_function




@app.route("/bye")
@make_bold
@make_emphasis
@make_underlined
def bye():
    return "See You Again!"







if __name__ == "__main__":
    # Run the app in debug mode to auto-reload
    app.run(debug=True)                                                    # equal to 'flask run'

    