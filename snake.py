from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.game_snake = []
        self.create_snake()
        self.head = self.game_snake[0]

    def create_snake(self):
        for i in STARTING_POSITION:
            self.add_segment(i)

    def add_segment(self, i):
        snake = Turtle('square')
        snake.penup()
        snake.color('white')
        snake.goto(i)
        self.game_snake.append(snake)

    def extend_snake(self):
        # add a new segment
        pos = len(self.game_snake) - 1
        self.add_segment(self.game_snake[pos].position()) # we are picking the position of the last segment of the snake here and adding a segment at its position

    def move(self):
        for i in range(len(self.game_snake) - 1, 0, -1):
            new_x = self.game_snake[i - 1].xcor()
            new_y = self.game_snake[i - 1].ycor()
            self.game_snake[i].goto(new_x, new_y)
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
