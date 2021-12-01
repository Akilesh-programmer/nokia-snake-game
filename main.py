# Importing the turtle class and screen class from turtle module.
from turtle import Screen, Turtle

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

# Having a list full of x and y coordinates position for my initial three squares in the game.
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

# Then creating a list to store the created objects.
segments = []

# Creating the three squares with a for loop.
for position in starting_positions:
    # First creating the object along with specifiying its shape.
    new_segment = Turtle(shape="square")
    # Taking the pen up from the squares so that they won't draw a line when the move.
    new_segment.penup()
    # Then chaing the color of the new square.
    new_segment.color("white")
    # Then setting the position of the square. Here we need to remember that each square by default will have a size of 20 x 20 pixels.
    new_segment.goto(position)
    # Appending the newly created object to the segments list.
    segments.append(new_segment)
    

# Updating the screen.
screen.update()

# Creating a boolean variable to show that game is on.
game_is_on = True

# Creating a while loop to run the game that is to move the squares.
while game_is_on:
    # Then with a for loop moving the squares by 10 pixels.
    for segment in segments:
        segment.forward(20)
    

# Updating the screen.
screen.update()












# Using a method to close the screen only when we click on it.
screen.exitonclick()