from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

def end_game():
    global isGameOn
    isGameOn = False

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(end_game, "x")

isGameOn = True
while isGameOn:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect Collision with food
    if snake.head.distance(food) < 15:
        # food is 10 x 10
        food.refresh()
        snake.extend()
        scoreboard.increaseScore()

    # Detect Collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280 :
        scoreboard.reset()
        snake.reset()

    # Detect Collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

