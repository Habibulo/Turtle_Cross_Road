from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.score = 0
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=("Courier", 50, "normal"))

    def update_scoreboard(self):
        self.clear()
        self.goto(-300, 370)
        self.write(f"Score: {self.score}", align="center", font=("Courier", 20, "normal"))

    def point(self):
        self.score += 1
        self.update_scoreboard()