from turtle import Turtle, Screen, forward, backward, right, left
from random import choice, randint
from turtle import colormode



colormode(255)
slowy = Turtle()
my_screen = Screen()
angles = [90, 180, 270, 0]
my_screen.bgcolor("gray")
def change_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    Tuple = (r, g, b)
    return Tuple
slowy.speed(9)
slowy.pensize(10)
for _ in range (200):
    slowy.forward(20)
    slowy.right(choice(angles))
    slowy.color(change_color())











my_screen.exitonclick()

