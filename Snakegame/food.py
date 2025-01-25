from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.up()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('yellow')
        x_pos = random.randint(-320, 320)
        y_pos = random.randint(-320, 300)
        self.goto(x_pos,y_pos)
        self.newfood()

    def newfood(self):
        x_pos = random.randint(-320, 320)
        y_pos = random.randint(-320, 300)
        self.goto(x_pos, y_pos)
    
    