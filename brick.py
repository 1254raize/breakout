import random
from turtle import *


class Brick(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random_color())
        self.shapesize(stretch_len=2.7)
        self.penup()

    def remove_brick(self):
        self.hideturtle()


def random_color():
    red = random.randint(0,255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    color_rgb = (red, green, blue)
    return color_rgb

