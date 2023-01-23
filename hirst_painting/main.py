# import colorgram as cg
#
#
# colors = cg.extract('hirst_painting_sample.jpeg', 12)
# my_colors = []
#
#
# for i in range(12):
#     r = colors[i].rgb.r
#     g = colors[i].rgb.g
#     b = colors[i].rgb.b
#     my_tuple = (r, g, b)
#     my_colors.append(my_tuple)
#
# print(my_colors)
from turtle import Turtle, Screen, colormode
from random import choice
slowy = Turtle()
slowy.hideturtle()
screen = Screen ()
colormode(255)

my_colors = [(195, 164, 13), (201, 75, 15), (231, 54, 132), (110, 179, 216), (217, 163, 101), (27, 105, 168)]

slowy.shape("turtle")
slowy.penup()
Y = -300
slowy.setpos(-300, Y)
for i in range(10):
    for j in range(10):
        slowy.dot(20, choice(my_colors))
        slowy.fd(50)
    Y += 50
    slowy.setpos(-300, Y)


screen.exitonclick()
