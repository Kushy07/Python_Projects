from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5, outline=10)
        # Here stretching means 0.5 of the 20px = 10px
        self.pencolor("blue")
        self.speed("fastest")
        self.refresh()
        # or speed could be 0 (fastest)

    def refresh(self):
        x_cor = random.randint(-280, 280)
        y_cor = random.randint(-280, 280)
        self.goto(x_cor, y_cor)

