from turtle import Turtle, Screen

# Create a turtle object
x = Turtle()

# Function to draw a triangle
def draw_triangle(side_length):
    for _ in range(3):  # A triangle has 3 sides
        x.forward(side_length)  # Move forward by the length of one side
        x.right(120)  # Turn right by 120 degrees

# Draw a triangle with each side of length 100
draw_triangle(100)

# Function to draw a square
def draw_square(side):
    for _ in range(4):
        x.forward(side)  # Corrected from foward to forward
        x.right(90)    
def draw_pentagon(a):
    for _ in range(5):
        x.forward(a)  # Corrected from foward to forward
        x.right(72)   
draw_pentagon(100)
def draw_hexagon(b):
    for _ in range(6):
        x.forward(b)  # Corrected from foward to forward
        x.right(60)  
draw_hexagon(100)
def draw_heptagon(c):
    for _ in range(7):
        x.forward(c)  # Corrected from foward to forward
        x.right(51.42)   
draw_heptagon(100)
def draw_octagon(d):
    for _ in range(8):
        x.forward(d)  # Corrected from foward to forward
        x.right(45)   
draw_octagon(100)   

# Draw a square with each side of length 100
draw_square(100)

# Create a screen object and wait for a click to exit
screen = Screen()
screen.exitonclick()
