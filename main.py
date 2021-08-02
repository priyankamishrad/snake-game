from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My snake game")
screen.tracer(0)
is_game_on = True

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Listen to keystrokes
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect if snake spots food
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        food.change_position()
        snake.extend_snake()

    # Detect if snake hits the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        is_game_on = False
        scoreboard.game_over()

    # Detect if snake hits its tail
    for i in snake.game_snake[1:]:
        if snake.head.distance(i) < 10:
            is_game_on = False
            scoreboard.game_over()

screen.exitonclick()
