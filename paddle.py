from turtle import Turtle

UP = 90
DOWN = 270


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=4, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(x, y)
        self.turn = 1

    def up(self):
        if 220 >= self.ycor():
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() >= -220:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)

    def move(self):
        if self.turn == 1:
            self.up()
        else:
            self.down()

    def auto_move(self):
        if 200 < self.ycor() or self.ycor() < -200:
            self.turn = ~self.turn
        self.move()
