from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "left"
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.penup()
        # self.color("black")
        self.goto(-260, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"LEVEL:{self.score}", False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", False, align='center', font=FONT)
