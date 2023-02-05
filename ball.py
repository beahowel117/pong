from turtle import Turtle
import random

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        print('x', new_x)
        new_y = self.ycor() + self.y_move
        print('y', new_y)
        self.goto(new_x, new_y)

#bouncing off top and bottom wall
    def bounce_y(self):
        self.y_move *= -1

#bouncing off paddle
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()