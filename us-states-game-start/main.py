import turtle
import turtle as t
import pandas as pd

screen = t.Screen()
screen.title("U.S. States Guessing Game")
image = "us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("us-states-game-start/50_states.csv")

states_list = data.state.to_list()
guessed_states=[]

answer_state = turtle.textinput(prompt="What's another state's name?", title="Guess the State").title()

write = turtle.Turtle()
write.pu()
write.hideturtle()
correct_guess = 0
game_over = True
while game_over:
    if answer_state == "Exit":
        game_over = False
    if answer_state in states_list:
        correct_guess += 1
        guessed_states.append(answer_state)
        states_list.remove(answer_state)
        xcor = int(data[data.state == answer_state].x.item())
        ycor = int(data[data.state == answer_state].y.item())
        write.goto(xcor, ycor)
        write.write(answer_state)
    answer_state = turtle.textinput(prompt="What's another state's name?",
                                    title=f"{correct_guess}/50 States Correct").title()
    if correct_guess == 50:
        game_over = False

# states to learn csv
state_dict = {
    "States to be learned": states_list,

    }
print(guessed_states)
pd.DataFrame(state_dict).to_csv("states_to_be_revised.csv")

screen.exitonclick()
