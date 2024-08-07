from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_spd = 5
        self.y_spd = 5

    def
    def ball_loop(self, r_ycor, l_ycor):
        w = 40
        new_xcor = self.xcor() + self.x_spd
        new_ycor = self.ycor() + self.y_spd
        self.goto(new_xcor, new_ycor)

        if self.ycor() >= 290:
            self.y_spd = -self.y_spd
        if self.ycor() <= -290:
            self.y_spd = -self.y_spd
        if 340 >= self.xcor() >= 340-self.x_spd and (r_ycor - w) <= self.ycor() <= (r_ycor + w):
            self.x_spd = -self.x_spd
        if -340 <= self.xcor() <= -(340-self.x_spd) and (l_ycor - w) <= self.ycor() <= (l_ycor + w):
            self.x_spd = -self.x_spd


