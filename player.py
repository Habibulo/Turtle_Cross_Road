from turtle import Turtle
Finish_line = 380
Starting_Position = (0, -380)


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.left(90)
        self.setposition(Starting_Position)
        self.go_up()
        # self.is_at_finish()
    def go_up(self):
        self.forward(20)
    def go_to_start(self):
        self.goto(Starting_Position)
    def is_at_finish(self):
        if self.ycor() > Finish_line:
            return True
        else:
            return False
