from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

FONT = ("Times New Roman", 35, "normal")
FONT1 = ("Times New Roman", 20, "normal")
NAME = "SNAKE GAME"


def game_start():
    turtle.clear()
    turtle.hideturtle()
    turtle1.clear()
    turtle1.hideturtle()
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    screen.update()
    game_on = True
    while game_on:
        screen.update()
        time.sleep(0.1)
        snake.move_snake()
        # detect collision with food
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend_snake()
            scoreboard.increase_score()

        # detect collision with wall
        if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
            game_on = False
            scoreboard.game_over()

        # detect collision with tail
        for sec in snake.snake_bodies:
            if sec == snake.head:
                pass
            elif snake.head.distance(sec) < 10:
                game_on = False
                scoreboard.game_over()


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snakes")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
turtle = Turtle()
turtle.color("white")
turtle.write(NAME, align="center", font=FONT)
turtle1 = Turtle()
turtle1.color("white")
turtle1.goto(0, -240)
turtle1.write("Enter space to start!!", align="center", font=FONT1)
screen.onkey(game_start, "space")
screen.exitonclick()
