from turtle import Turtle
LOWEST_POSITION = -235
UPPER_POSITION = 235
STEP = 20


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(position)
        self.shapesize(stretch_wid=5, stretch_len=1)

    def up(self):
        if self.ycor() <= UPPER_POSITION:
            y_pos = self.ycor() + STEP
            self.goto(self.xcor(), y_pos)

    def down(self):
        if self.ycor() >= LOWEST_POSITION:
            y_pos = self.ycor() - STEP
            self.goto(self.xcor(), y_pos)
