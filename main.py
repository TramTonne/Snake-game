from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0) #tracer, update are used to let the computer know when to show the turtle change, instead of changing in every line of code

#create a snake body
snake=Snake()

food= Food()

score_board = ScoreBoard()

#snake movement according to up,down,left,right key
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    #snake movement
    snake.move()
    #detect collision with food
    #the distance of the snake's head from the food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.score_increment()

    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()<-290 or snake.head.ycor()>290:
        score_board.reset()
        snake.reset()

    #detect if the snake collide with itself
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            score_board.reset()
            snake.reset()
screen.exitonclick()