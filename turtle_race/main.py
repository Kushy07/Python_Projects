from turtle import Turtle, Screen
from random import randint


screen = Screen()
screen.setup(width=500, height=400)
colors = ['red', 'yellow', 'green', 'purple', 'orange', 'blue']
turtle_names = ['A', 'B', 'C', 'D', 'E', 'F']
turtles = {'A': 'red',
            'B': 'orange',
            'C': 'green',
            'D': 'purple',
            'E': 'orange',
            'F': 'blue'

}
turtle_list = []
for i in turtle_names:
    i = Turtle("turtle")
    i.penup()
    turtle_list.append(i)
i = 0
for k in turtle_list:
    k.color(colors[i])
    i += 1

#print(turtle_list)
X = -140
Y = -140
for i in turtle_list:
    i.goto(X, Y)
    Y = Y + 50


user_bet = screen.textinput(title="Make your bet", prompt="Which color do you choose?")

end_of_game = False
if user_bet:
    while not end_of_game:

        for slowy in turtle_list:
            if slowy.xcor()>230:
                if slowy.color == user_bet:
                    print(f'Congrats! You have won! {slowy.pencolor().capitalize()} has won the game!')
                    end_of_game = True
                else:
                    print(f"Oops! You have lost! {slowy.pencolor().capitalize()} has won the game!")
                    end_of_game = True

            slowy.forward(randint(0,6))







screen.exitonclick()


