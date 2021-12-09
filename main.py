from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")

screen.tracer(0) 

game_is_on = True

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)


def game_over():
    global snake
    scoreboard.game_over()
    scoreboard.reset()
    snake = Snake()
    

variable1 = -260
variable2 = 260
variable3 = -260
variable4 = 260


while game_is_on:
    screen.listen()
    screen.onkey(key="Up", fun=snake.up)
    screen.onkey(key="Down", fun=snake.down)
    screen.onkey(key="Left", fun=snake.left)
    screen.onkey(key="Right", fun=snake.right)
    screen.update()
    time.sleep(0.1)

    snake.move()
    
    

    # Detecting collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        

    # Detect collision with wall.
    if snake.head.xcor() > 280:
        for segment in snake.segments:
            variable1 -= 20
            segment.goto(variable1, 0)
        variable1 = -260
    elif snake.head.xcor() < -280:
        for segment in snake.segments:
            variable2 +=20
            segment.goto(variable2, 0)
        variable2 = 260
    elif snake.head.ycor() > 280:
        for segment in snake.segments:
            variable3 -= 20
            segment.goto(0, variable3)
        variable3 = -260
    elif snake.head.ycor() < -280:
        for segment in snake.segments:
            variable4 += 20
            segment.goto(0, variable4)
        variable4 = 260
    
    
        

    # Detect collisions with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            
            for segment in snake.segments:
                segment.goto(-1000, 1000)
                segment.clear()
            snake.head.clear()
            snake = 0
            game_over()
            scoreboard.score = 0
            scoreboard.update_scoreboard()
    # If head collides with any segment in the tail.
    
    if scoreboard.score > scoreboard.high_score:
        scoreboard.high_score = scoreboard.score
        scoreboard.clear()
        scoreboard.update_scoreboard()
        screen.update()

    screen.listen()
    screen.onkey(key="Up", fun=snake.up)
    screen.onkey(key="Down", fun=snake.down)
    screen.onkey(key="Left", fun=snake.left)
    screen.onkey(key="Right", fun=snake.right)

    

screen.exitonclick()
