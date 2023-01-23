from turtle import Turtle


ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")

with open("data.txt", mode="r") as file:
    data = file.read()


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()

        self.init_score = 0
        self.high_score = int(data)
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Your score: {self.init_score} High Score: {self.high_score}", align=ALIGNMENT, move=False, font=FONT)

    def up_score(self):
        self.init_score += 1

        self.update_scoreboard()

    def reset(self):
        if self.init_score > self.high_score:
            self.high_score = self.init_score
            with open("data.txt", mode = "w") as data:
                data.write(f"{self.high_score}")
        self.init_score = 0
        self.update_scoreboard()




    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", font=("Courier", 25, "bold"), align="center")
