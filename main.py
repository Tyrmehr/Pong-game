from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(fun=left_paddle.move_up, key="w")
screen.onkey(fun=left_paddle.move_down, key="s")
screen.onkey(fun=right_paddle.move_up, key="Up")
screen.onkey(fun=right_paddle.move_down, key="Down")

game_is_on = True

while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()

    ball.move_ball()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.hit_wall()

    if (ball.xcor() > 320 and ball.distance(right_paddle) < 40) or (ball.xcor() < -320 and ball.distance(left_paddle) < 40):
        ball.hit_paddle()

    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.left_scored()

    if ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.right_scored()




screen.exitonclick()
