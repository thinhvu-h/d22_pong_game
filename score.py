from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.color("White")
        self.penup()
        self.hideturtle()

        for midline in range(-260, 280, 10):
            self.goto(0, midline)
            self.write("|", False, align="center", font=('Arial', 12, 'normal'))

        self.score = 0
        self.goto(x, y)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.score}", False, align="center", font=('Arial', 100, 'normal'))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()