from turtle import *


class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.hideturtle()
        self.penup()
        self.shape("square")
        self.color("white")
        self.shapesize(0.2, 5, 10)
        self.setpos(0, -345)
        self.setheading(180)
        self.showturtle()
        self.speed("fastest")

        listen()

        onkey(self.move_left, 'Left')
        onkey(self.move_right, 'Right')

    def move_left(self):
        self.forward(50)

    def move_right(self):
        self.back(50)
