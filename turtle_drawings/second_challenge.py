from turtle import Turtle, Screen
from random import choice
slowy = Turtle()
my_screen = Screen()
my_screen.bgcolor("lightgreen")
slowy.speed(1)
slowy.pensize(10)
colors = ['red', 'yellow', 'green', 'blue', 'black', 'cyan', 'deep pink', 'pink']
side = [3, 4, 5, 6, 7, 8, 9, 10]
angle = [120, 90, 72, 60, 51.43, 45, 40, 36]
mapping = {
3:120,4:90,5:72,6:60,7:51.43,8:45,9:40,10:36
}
for i in side:
    for j in range(i):
        slowy.forward(100)
        slowy.right(mapping[i])
    slowy.color(choice(colors))

my_screen.exitonclick()

