from turtle import *


class Ball(Turtle):
    def __init__(self, player, bricks, score):
        super(Ball, self).__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setpos(0, -326)
        self.in_motion = False
        self.direction = [3, 3]
        self.player = player
        self.bricks = bricks
        self.score = score

        listen()

        onkeypress(self.set_on_motion, 'space')

    def set_on_motion(self):
        self.in_motion = True

        while self.in_motion:

            current_pos = self.pos()
            for brick in self.bricks:

                if self.pos()[1] > 0:
                    if abs(self.pos()[0] - brick.pos()[0]) <= 35 and abs(self.pos()[1] - brick.pos()[1]) <= 15:
                        print("TOUCH")
                        self.score.score += 1
                        self.score.update_score()
                        self.reverse_up_down()
                        brick.remove_brick()
                        self.bricks.remove(brick)
                        self.setpos(current_pos[0] + self.direction[0], current_pos[1] + self.direction[1])

            self.setpos(current_pos[0] + self.direction[0], current_pos[1] + self.direction[1])
            if self.pos()[0] >= 502 or self.pos()[0] <= -502:
                self.reverse_right_left()
            if self.pos()[1] >= 360:
                self.reverse_up_down()
            if self.pos()[1] <= -340:
                self.direction = [0, 0]
            if abs(self.pos()[0] - self.player.pos()[0]) <= 50 and abs(self.pos()[1] - self.player.pos()[1]) <= 10:
                self.reverse_up_down()

    def reverse_right_left(self):
        self.direction[0] *= -1

    def reverse_up_down(self):
        self.direction[1] *= -1

    def stop_motion(self):
        self.direction = [0, 0]
