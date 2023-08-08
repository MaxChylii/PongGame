from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed(0)
        self.move_distance_x = 10
        self.move_distance_y = 10
        self.move_speed = 0.1

    def hit_the_wall(self):
        self.move_distance_y *= -1

    def hit_the_paddle(self):
        self.move_distance_x *= -1
        self.move_speed *= 0.9

    def move(self):
        new_x = self.xcor() + self.move_distance_x
        new_y = self.ycor() + self.move_distance_y
        self.goto(new_x, new_y)

    def reset_position(self):
        self.home()
        self.move_speed = 0.1
        self.hit_the_paddle()
