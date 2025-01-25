import random
from turtle import Turtle
import random
BRICK_COLORS = ['red', 'yellow', 'navy', 'sky blue', 'orange', 'teal', 'green']
BRICK_PACE = 7


class Bricks:
    def __init__(self):
        self.bricks_list = []
        self.brick_speed = BRICK_PACE

    def create_bricks(self):                     # Create bricks
        choice = random.randint(1, 10)
        if choice == 1 or choice == 10:
            new_brick = Turtle(shape='square')
            new_brick.up()
            new_brick.shapesize(stretch_wid=1.5, stretch_len=3)
            new_brick.color(random.choices(BRICK_COLORS))
            new_brick.setheading(180)
            y_pos = random.randint(-200, 230)
            new_brick.goto(330, y_pos)
            self.bricks_list.append(new_brick)

    def move(self):
        for brick in self.bricks_list:        # Move the brick
            brick.fd(self.brick_speed)

    def brick_speed_up(self):                # Speed up the brick when level up
        self.brick_speed += BRICK_PACE

