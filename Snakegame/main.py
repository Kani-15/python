import turtle as t
import time
from snake import Snake
from food import Food
from scoreboard import Score
screen = t.Screen()
screen.setup(700, 700)
screen.bgcolor("white")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()
t.color('black')
t.hideturtle()

game = True


screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')
# screen.onkey(snake.pause, "space")
# screen.onkey(snake.play, "a")

while game:
    screen.update()
    time.sleep(0.15)
    snake.move()
    if snake.head.distance(food) < 15:
        score.score += 1
        score.update_score()
        snake.update_snake_size()
        food.newfood()

    # detect collision with the wall
    if snake.head.xcor() > 340 or snake.head.xcor() < -340 or snake.head.ycor() > 300 or snake.head.ycor() < -340:
        score.reset_score()
        snake.reset_snake()
        # game = False
        # t.write("Game Over", align="center", font=("Comic Sans MS", 30, "bold"))
        # t.goto(0, -30)
        # t.color('white')
        # t.write(f"Your Score: {score.score}", align="center", font=("Comic Sans MS", 15, "bold"))

    # detect collision with tail
    for segment in snake.new_segment[1: len(snake.new_segment) - 1]:
        if snake.head.distance(segment) < 10:
            score.reset_score()
            snake.reset_snake()
            # game = False
            # t.write("Game Over", align="center", font=("Comic Sans MS", 30, "bold"))
            # t.goto(0, -30)
            # t.color('white')
            # t.write(f"Your Score: {score.score}", align="center", font=("Comic Sans MS", 15, "bold"))
screen.exitonclick()

