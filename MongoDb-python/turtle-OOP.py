from turtle import Screen, Turtle


new_turtle = Turtle()                                          # 2. choice:  new_turtle = turtle.Turtle()
new_turtle.shape("turtle")
new_turtle.color("red", "green")


##################################################

def triangle_turtle():
    new_turtle.forward(100)
    new_turtle.right(120)


for a in range(3):
    triangle_turtle()

##################################################


def square_turtle():
    new_turtle.forward(100)
    new_turtle.right(90)


for i in range(4):
    square_turtle()
##################################################


def pentagon_turtle():
    new_turtle.forward(100)
    new_turtle.right(72)


for j in range(5):
    pentagon_turtle()

##################################################


def hexagon_turtle():
    new_turtle.forward(100)
    new_turtle.right(60)


for k in range(6):
    hexagon_turtle()


##################################################
def heptagon_turtle():
    new_turtle.forward(100)
    new_turtle.right(51.43)


for m in range(7):
    heptagon_turtle()


##################################################
def octagon_turtle():
    new_turtle.forward(100)
    new_turtle.right(45)


for n in range(8):
    octagon_turtle()

#################################################


def nonagon_turtle():
    new_turtle.forward(100)
    new_turtle.right(40)


for o in range(9):
    nonagon_turtle()
################################################


def decagon_turtle():
    new_turtle.forward(100)
    new_turtle.right(36)


for p in range(10):
    decagon_turtle()


Screen().exitonclick()
