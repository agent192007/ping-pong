from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("ping pong")
screen.tracer(0)

r_paddle = Paddle('Up', 'Down', 350)
l_paddle = Paddle('w', 's', -350)
ball = Ball()

screen.update()

loop = True

r_paddle.paddle_loop(screen)
l_paddle.paddle_loop(screen)

while loop:
    ball.ball_loop(r_paddle.ycor(),l_paddle.ycor())
    screen.update()
    time.sleep(0.025)

screen.exitonclick()
