import turtle as t

INITIAL_POSITION = [(0, 0), (-20, 0), (-40, 0)]
PACE = 20


class Snake:
    def __init__(self):
        self.new_segment = []
        self.snake()
        self.head = self.new_segment[0]
        self.head.color('white')

    def snake(self):
        for i in INITIAL_POSITION:
            self.add_segmenst(i)

    def add_segmenst(self, pos):
        snake_segment = t.Turtle(shape="circle")
        snake_segment.color("green")
        snake_segment.up()
        snake_segment.goto(pos)
        self.new_segment.append(snake_segment)

    def update_snake_size(self):
        self.add_segmenst(self.new_segment[-1].position())

    def move(self):
        for i in range(len(self.new_segment) - 1, 0, -1):
            x = self.new_segment[i - 1].xcor()
            y = self.new_segment[i - 1].ycor()
            self.new_segment[i].goto(x, y)
        self.new_segment[0].fd(PACE)

    def reset_snake(self):
        for i in self.new_segment:
            i.goto(700,700)
        self.new_segment.clear()
        self.snake()
        self.head = self.new_segment[0]
        self.head.color('white')

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)



