import turtle as t
import time
from player_turtle import Player
from bricks import Bricks
from scoreboard import Score

screen = t.Screen()
screen.setup(height=600, width=600)
screen.tracer(0)
screen.bgcolor('grey')

level = 1
player = Player()
bricks = Bricks()
score = Score()


t.color('black')
t.up()
t.goto(-300, 260)
for i in range(50):
    t.down()
    t.fd(10)
    t.up()
    t.fd(10)
t.goto(0,0)
t.hideturtle()


game = True
screen.listen()
screen.onkey(player.move, 'Up')

while game:
    time.sleep(0.1)
    screen.update()
    bricks.create_bricks()
    bricks.move()
    for brick in bricks.bricks_list:
        if brick.distance(player) < 20:
            t.write("Game Over", align='center', font=('Times New Roman', 30, "bold"))
            game = False
    if player.ycor() > 260:
        player.goto(0, -280)
        level += 1
        score.level_up(level)
        bricks.brick_speed_up()

screen.exitonclick()
