from turtle import *# Imports all functions and classes from the Turtle graphics library, which is used for drawing graphics.
from random import randrange#generates random numbers
from freegames import square, vector#square-shapes and vecotr-handling coordinates

food = vector(0, 0)#food initialised at origin
snake = [vector(10, 0)]#initial posn of snake
aim = vector(0, -10)#snakes initialized to move downward,easier choice

def change(x, y):#new dirn for snake
    aim.x = x
    aim.y = y

def inside(head):#The inside function checks if the snake's head is out of bounds and, if so, wraps it around to the opposite side of the screen, ensuring continuous gameplay within the defined boundaries.
    if head.x < -200:
        head.x = 190
    elif head.x > 190:
        head.x = -200
    if head.y < -200:
        head.y = 190
    elif head.y > 190:
        head.y = -200
    return True

def move():#creates a copy of the current head of the snake and moves it in the direction specified by the aim vector.
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:#to check if gameover
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)#calls again after 100 milliseconds, creating a loop that keeps the game running

setup(420, 420, 370, 0)
hideturtle()# Hides the turtle cursor, which is not needed for this game.
tracer(False)# Disables automatic screen updates to improve performance, allowing manual control of when to update the screen
listen()#: Prepares the window to listen for keyboard events.
onkey(lambda: change(10, 0), 'Right')#all four for arrow keys
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
