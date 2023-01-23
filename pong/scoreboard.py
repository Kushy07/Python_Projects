from turtle import Turtle


ALIGNMENT = "center"
FONT = ("Courier", 38, "bold")


class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.init_score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"{self.init_score}", align=ALIGNMENT, move=False, font=FONT)

    def up_score(self):
        self.init_score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self, who):
        self.goto(0,0)
        self.write(arg=f"Game over! {who} wins", align=ALIGNMENT, move=False, font=("courier", 25, "bold"))