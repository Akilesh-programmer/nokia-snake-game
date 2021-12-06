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
    scoreboard.game_over()
    food.game_over()

variable1 = -280
variable2 = 280
variable3 = -280
variable4 = 280

while game_is_on:
    

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
        variable1 = -280
    elif snake.head.xcor() < -280:
        for segment in snake.segments:
            variable2 +=20
            segment.goto(variable2, 0)
        variable2 = 280
    elif snake.head.ycor() > 280:
        for segment in snake.segments:
            variable3 -= 20
            segment.goto(0, variable3)
        variable3 = -280
    elif snake.head.ycor() < -280:
        for segment in snake.segments:
            variable4 += 20
            segment.goto(0, variable4)
        variable4 = 280
    
    
        

    # Detect collisions with tail.
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            game_over()
    # If head collides with any segment in the tail.
    

    screen.update()
    time.sleep(0.1)

    

screen.exitonclick()