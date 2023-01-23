from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


sb = Scoreboard()
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

# turn animation off. Until we're not going to update the screen won't refresh
# and not going to show us the animation which
# on the screen
screen.tracer(0)

snake = Snake()
food = Food()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
segments = []

game_is_on = True

while game_is_on:
    # when to refresh the screen
    screen.update()
    # 0.1 sec delay after each segment moves
    time.sleep(0.1)
    snake.move()
    # Now, we can move the head wherever we want it to move
    # Now, let's detect collision with food

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        sb.up_score()

    # Let's detect collision with wall

    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        sb.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        # if slicing is not performed. Start with elif
        # if snake.head.position() == segment.position():
        #     pass

        if snake.head.distance(segment) < 10:
            sb.reset()
            snake.reset()




screen.exitonclick()
