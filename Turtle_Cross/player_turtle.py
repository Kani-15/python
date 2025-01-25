from turtle import Turtle

START = (0, -280)
PACE_DISTANCE = 10
FINISH = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.up()
        self.goto(0, -280)
        self.setheading(90)
        self.move()

    def move(self):
        self.fd(PACE_DISTANCE)

