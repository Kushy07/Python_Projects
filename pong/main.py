from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")


screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

ball = Ball()
l_sb = Scoreboard((-50, 250))
r_sb = Scoreboard((50, 250))


mid_line = Turtle()
mid_line.shapesize(stretch_wid=0.5, stretch_len=2)
mid_line.shape("square")
mid_line.color("white")
mid_line.penup()
mid_line.setposition(0, 280)
mid_line.setheading(270)
for i in range(30):
    mid_line.pendown()
    mid_line.forward(10)
    mid_line.penup()
    mid_line.forward(10)


game_is_on = True

while game_is_on:
    screen.update()

    time.sleep(ball.move_speed)

    ball.move()

    if l_sb.init_score == 10:

        l_sb.game_over("L")
        game_is_on = False

    elif r_sb.init_score == 10:
        print("R wins!")
        r_sb.game_over("R")
        game_is_on = False
    # collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # need to bounce
        ball.bounce_y()
    elif ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

        # detect when right_paddle misses
    elif ball.xcor() > 380:
        ball.reset_position()
        l_sb.up_score()
        # detect when left_paddle misses
    elif ball.xcor() < -380:
        ball.reset_position()
        r_sb.up_score()


screen.exitonclick()
