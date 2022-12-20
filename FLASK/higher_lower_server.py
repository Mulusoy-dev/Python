from flask import Flask
import random
app = Flask(__name__)






@app.route('/')
def hello_world():                                                               # HTML and CSS redering in Flask 
    return '<h1 style="color:red;">Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'                            
            




@app.route('/URL/<int:value>')
def number_game(value):
    random_val = random.randint(0,9)
    print(random_val) 
    if value < random_val:
        return '<h1>Too low, try again!</h1>' \
                '<img src="https://media.giphy.com/media/cS83sLRzgVOeY/giphy.gif" width=300>'
    elif value > random_val:
        return '<h1>Too high, try again!</h1>' \
                '<img src="https://media.giphy.com/media/YsTs5ltWtEhnq/giphy.gif" width=300>'
    else:
        return '<h1>You found me!</h1>' \
                '<img src="https://media.giphy.com/media/o75ajIFH0QnQC3nCeD/giphy.gif" width=300>'





@app.route("/username/<name>")                                            # <name> str Type
def greet(name):
    return f"Welcome {name}!"


@app.route("/<name>/<int:number>")                                         # <int> int Type
def info(name, number):
    return f"Hello {name} you are {number} years old."











if __name__ == "__main__":
    # Run the app in debug mode to auto-reload
    app.run(debug=True)                                                    # equal to 'flask run'
