import turtle

import pandas
from turtle import Turtle, Screen

screen = Screen()
screen.title("U.S. States Game")
image = "/Users/melih/PycharmProjects/us-states-game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


df = pandas.read_csv("/Users/melih/Downloads/us-states-game-start/us-states-game-start/50_states.csv")
print(df)
data_list = df.state.to_list()
print(data_list)
guessed_state = []


while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 States Correct",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = []
        for state in data_list:
            if state not in guessed_state:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in data_list:
        guessed_state.append(answer_state)
        new_t = turtle.Turtle()
        new_t.penup()
        new_t.hideturtle()
        state_data = df[df.state == answer_state]
        new_t.goto(int(state_data.x), int(state_data.y))
        new_t.write(answer_state)








screen.exitonclick()