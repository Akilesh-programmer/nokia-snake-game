# Importing the turtle class and screen class from turtle module.
from turtle import Screen, Turtle
import snake
# Importing time module.
import time
# Creating a screen object. This is gonna be the window that shows up.
screen = Screen()

# Setting the height and width of the screen.
screen.setup(height=600, width=600)

# Changing the background color of the screen.
screen.bgcolor("black")

# Setting a title for the screen.
screen.title("Snake Game")

# When we are playing the snake game then we could see some animations, they are not needed and they don't look good. For example we will be three squares, they won't come up all at the same time, first the first one will be drawn, next the next one will be drawn, so we could see that animation. We can turn that off with the help of the below method associated with screen. Also we need to say when we want to update the screen, that it to show changes, so that at that line of code only the entire new thing will be printed. So we don't see the animation. We need to give the paramater to zero to turn the animation off.
screen.tracer(0)



# Updating the screen.
screen.update()

sup = snake.Snake()

# Creating a boolean variable to show that game is on.
game_is_on = True

# Creating a while loop to run the game that is to move the squares.
while game_is_on:
    screen.update()
    time.sleep(1)
    sup.forward()
    sup.forward()
    screen.update()
    sup.turn_right()








            







# Using a method to close the screen only when we click on it.
screen.exitonclick()