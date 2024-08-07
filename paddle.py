from turtle import Turtle
import turtle


class Paddle(Turtle):
    def __init__(self,up,down,x):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=4)
        self.goto(x, 0)
        self.left(90)
        self.up_key = up
        self.down_key = down

    def paddle_loop(self, screen):
        def move(key):
            if key == "up" and self.ycor() < 260:
                self.goto(self.xcor(), self.ycor() + 10)
            elif key == "down" and self.ycor() > -260:
                self.goto(self.xcor(), self.ycor() - 10)
            screen.update()

        turtle.onkeypress(lambda: move("up"), self.up_key)
        turtle.onkeypress(lambda: move("down"), self.down_key)
        turtle.listen()
        print(self.ycor())
