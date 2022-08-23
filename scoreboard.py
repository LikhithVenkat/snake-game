from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Times New Roman", 20, "normal")
FONT_G = ("Times New Roman", 24, "normal")


class Scoreboard(Turtle):
    # class to manage score
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score:{self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align=ALIGNMENT, font=FONT_G)
