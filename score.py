from turtle import *


class Score(Turtle):

    def __init__(self, score):
        self.score_turtle = Turtle()
        self.score_turtle.color("white")
        self.score_turtle.penup()
        self.score_turtle.hideturtle()
        self.score_turtle.goto(15, 320)

        super(Score, self).__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-70, 320)
        self.score = score
        self.write(f"Score: ", font=("Arial", 20, "normal"))

    def update_score(self):
        self.score_turtle.clear()
        self.score_turtle.write(self.score, font=("Arial", 20, "normal"))
