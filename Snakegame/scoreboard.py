from turtle import Turtle
with open(file='high_score.txt') as f:
    HIGH_SCORE = f.read()


class Score(Turtle):
    def __init__(self):
        super().__init__()

        tim = Turtle()
        tim.up()
        tim.goto(-350, -350)
        tim.down()
        tim.begin_fill()
        for _ in range(2):
            tim.forward(700)
            tim.left(90)
            tim.forward(700)
            tim.left(90)
        tim.end_fill()
        tim.color('yellow')
        tim.up()
        tim.goto(-350, 310)
        tim.down()
        for i in range(35):
            tim.fd(10)
            tim.up()
            tim.fd(10)
            tim.down()
        tim.hideturtle()

        self.score = 0
        self.high_score = int(HIGH_SCORE)
        self.color('yellow')
        self.up()
        self.goto(0, 320)
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Comic Sans MS", 15,
                                                                                               "bold"))
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align="center", font=("Comic Sans MS", 15,
                                                                                               "bold"))

    def reset_score(self):
        if self.high_score < self.score:
            self.high_score = self.score
            with open(file='high_score.txt', mode='w') as f:
                f.write(str(self.score))
        self.score = 0
        self.update_score()

