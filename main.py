
'''
Goal
    + ball
    + bar
    + bouncing
    + score
'''
import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

left_paddle = Paddle(-350, 0)
right_paddle = Paddle(350, 0)

ball = Ball()

left_scoreboard = Scoreboard(-100, 180)
right_scoreboard = Scoreboard(100, 180)

screen.onkey(key="Up", fun=right_paddle.up)
screen.onkey(key="Down", fun=right_paddle.down)
# screen.onkey(key="w", fun=left_paddle.up)
# screen.onkey(key="s", fun=left_paddle.down)
screen.onkeypress(key="a", fun=left_paddle.up)
screen.onkeypress(key="s", fun=left_paddle.down)
screen.listen()


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    right_paddle.auto_move()
    ball.move()

    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_wall()

    if ball.distance(left_paddle) < 50 and ball.xcor() <= -320 or \
            ball.distance(right_paddle) < 50 and ball.xcor() >= 320:
        ball.bounce_paddle()

    if ball.xcor() < -340:
        print("left miss the ball")
        ball.reset_position()
        right_scoreboard.increase_score()
    elif ball.xcor() > 340:
        print("right miss the ball")
        ball.reset_position()
        left_scoreboard.increase_score()

screen.exitonclick()