from turtle import Screen
from paddle import Paddle
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("ping pong")
screen.tracer(0)

r_paddle = Paddle('Up', 'Down',350)
l_paddle = Paddle('w', 's',-350)

screen.update()

loop = True

r_paddle.paddle_loop(screen)
l_paddle.paddle_loop(screen)

screen.exitonclick()
