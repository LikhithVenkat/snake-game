from turtle import Turtle

STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    # class to store or implement the members related to the behaviour of snake
    def __init__(self):
        self.snake_bodies = []
        self.create_snake()
        self.head = self.snake_bodies[0]

    def create_snake(self):
        for pos in STARTING_POS:
            self.add_snake(pos)

    def add_snake(self,pos):
        snake_body = Turtle("square")
        snake_body.color("green")
        snake_body.penup()
        snake_body.goto(pos)
        self.snake_bodies.append(snake_body)

    def extend_snake(self):
        self.add_snake(self.snake_bodies[-1].position())

    def move_snake(self):
        for seg in range(len(self.snake_bodies) - 1, 0, -1):
            x_cor = self.snake_bodies[seg - 1].xcor()
            y_cor = self.snake_bodies[seg - 1].ycor()
            self.snake_bodies[seg].goto(x_cor, y_cor)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
