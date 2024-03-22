from turtle import Turtle, Screen
import csv
import pandas

turtle = Turtle()

screen = Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

""" Using Pandas to read the csv file """
data_contents = pandas.read_csv("50_states.csv")
# print(data_contents)

""" List of all the states """
states = data_contents["state"].to_list()

""" While loop conditions """
guessed_state = []

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)} /50 correct",
                                    prompt="What's another state name? ").title()

    """ Using list comprehension """
    if answer_state == "Exit":
        missing_states_list = [i for i in states if i not in guessed_state]

        print("The states you missed are -> ", missing_states_list)

        """ To convert the dataframe dict to pandas """
        missed_states = pandas.DataFrame(missing_states_list)
        """ To create a csv file """
        missed_states.to_csv("states_to_learn.csv")
        break

    if answer_state in states:
        guessed_state.append(answer_state)
        """ Create a turtle """
        k = Turtle()
        k.hideturtle()
        k.penup()
        state_row = (data_contents[data_contents["state"] == answer_state])
        """ To get the state's x and y cor from csv file """
        k.goto(int(state_row.x.iloc[0]), int(state_row.y.iloc[0]))
        k.write(answer_state)
