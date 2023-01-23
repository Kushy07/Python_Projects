from turtle import Turtle, Screen
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


slowy.speed(0)
slowy.pensize(2)
def make_spirograph(size_of_gap):
    for _ in range(int(360/ size_of_gap)):
        slowy.circle(100)
        slowy.setheading(slowy.heading() + size_of_gap)
        slowy.color(change_color())

make_spirograph(5)

my_screen.exitonclick()

