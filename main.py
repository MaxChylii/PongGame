from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

# paint centered line
line = Turtle()
line.hideturtle()
line.speed(0)
line.penup()
line.goto(0, -300)
line.setheading(90)
line.pensize(8)
line.color("white")
for _ in range(13):
    line.pendown()
    line.forward(25)
    line.penup()
    line.forward(25)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

ball = Ball()
ball.hit_the_wall()

game_is_on = True
scoreboard = Scoreboard()

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect the collision with top or bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.hit_the_wall()

    # detect the collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.hit_the_paddle()
    elif ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.hit_the_paddle()

    # detect right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # detect left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    # finish the game
    if scoreboard.l_score == 10 or scoreboard.r_score == 10:
        game_is_on = False

screen.exitonclick()
