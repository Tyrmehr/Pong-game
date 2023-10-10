from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.write_score()

    def write_score(self):
        self.goto(-100, 200)
        self.write(arg=self.left_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(arg=self.right_score, align="center", font=("Courier", 80, "normal"))

    def left_scored(self):
        self.left_score += 1
        self.clear()
        self.write_score()

    def right_scored(self):
        self.right_score += 1
        self.clear()
        self.write_score()