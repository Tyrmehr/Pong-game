from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)

    def hit_wall(self):
        self.y_move *= -1

    def hit_paddle(self):
        self.x_move *= -1
        self.ball_speed *= 0.8

    def reset_ball(self):
        self.home()
        self.hit_paddle()
        self.ball_speed = 0.1
