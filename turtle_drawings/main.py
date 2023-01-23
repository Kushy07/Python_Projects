from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
screen = Screen()

timmy_the_turtle.shape('classic')
for _ in range(30):
    timmy_the_turtle.pendown()
    timmy_the_turtle.forward(10)
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(10)


screen.exitonclick()