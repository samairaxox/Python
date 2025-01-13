import turtle
import random

# Function to generate a random color
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# Function to draw the spirograph
def draw_spirograph(size_of_gap):
    for angle in range(0, 360, size_of_gap):
        tim.color(random_color())  # Set a random color
        tim.setheading(angle)       # Set the heading
        tim.circle(50)             # Draw a circle with radius 100

# Set up the turtle
turtle.colormode(255)  # Enable RGB color mode
tim = turtle.Turtle()
tim.speed(0)           # Fastest speed

# Draw the spirograph with a gap of 5 degrees
draw_spirograph(5)

# Finish up
turtle.done()
