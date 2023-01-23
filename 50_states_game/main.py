import turtle
import pandas as pd

screen = turtle.Screen()
screen.title('US States Game')
us_map = 'blank_states_img.gif'
screen.addshape(us_map)
turtle.shape(us_map)
count = 0
data = pd.read_csv('50_states.csv')

state = turtle.Turtle()
state.hideturtle()
state.penup()

ds = data.state.to_list()
my_list = []

game_is_on = True
while game_is_on:

    answer = screen.textinput(title=f"{count}/50 states correct", prompt="What's the state name? ")
    answer = answer.title()
    if answer in ds and count != 50 and answer not in my_list:
        count += 1
        my_list.append(answer)
        x_cor = data[data['state'] == answer]['x'].item()
        # or x_cor = int(data[data['state'] == answer]['x'])
        y_cor = data[data['state'] == answer]['y'].item()
        # print(x_cor, y_cor)
        state.goto(x_cor, y_cor)
        state.write(arg=f"{answer}", align="center", move=False, font=("Courier", 10, "bold"))

    elif count == 50:
        game_is_on = False

    elif answer =='Exit':
        missing_states = [state for state in ds if state not in my_list]
        # for state in ds:
        #     if state not in my_list:
        #         missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv('states_to_learn.csv')
        break
        
    elif answer in my_list:
        pass

    else:
        game_is_on = False





