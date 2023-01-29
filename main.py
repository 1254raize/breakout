import turtle
import random
from turtle import *
import brick
import player
import ball
import score

wn = turtle.Screen()
wn.colormode(255)
wn.bgcolor("black")
wn.title("Breakout")
wn.setup(width=1024, height=720)
wn.tracer(False)

score = score.Score(0)
bricks = []
starting_point_brick = [-483, 330]

for _ in range(5):
    starting_point_brick[1] -= 25
    for i in range(0, 18):
        new_brick = brick.Brick()
        new_brick.hideturtle()
        new_brick.speed(0)
        new_brick.setpos(starting_point_brick[0] + i * 60, starting_point_brick[1])
        new_brick.showturtle()
        bricks.append(new_brick)


player = player.Player()

ball = ball.Ball(player, bricks, score)

wn.tracer(True)
wn.mainloop()
