from turtle import Turtle, Screen

# Create a turtle object
timmy_the_turtle = Turtle()

# Change the turtle's shape and color
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("blue")

# Move the turtle in a square pattern
for _ in range(4):
    timmy_the_turtle.forward(100)  # Move forward by 100 units
    timmy_the_turtle.right(90)      # Turn right by 90 degrees

# Create a screen object and wait for a click to exit
screen = Screen()
screen.exitonclick()
