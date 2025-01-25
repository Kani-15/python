from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color('yellow')
        self.up()
        self.goto(-240,260)
        self.write(f"Level : {0}", align='center', font=('Times New Roman', 20, "bold"))
        self.hideturtle()


    def level_up(self,level):
        self.clear()
        self.write(f"Level : {level}", align='center', font=('Times New Roman', 20, "bold"))


