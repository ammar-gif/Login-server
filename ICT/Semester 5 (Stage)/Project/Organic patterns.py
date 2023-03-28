import turtle
import random

# Set the screen size and background color
turtle.setup(800, 600)
turtle.bgcolor("#ecf0f1")

# Create a turtle object
t = turtle.Turtle()

# Set the turtle's shape
t.shape("turtle")

# Set the turtle's speed
t.speed(10)

# Set the turtle's pen color and size
t.pencolor("#e74c3c")
t.pensize(5)

# Set the turtle's starting position
t.penup()
t.setpos(0,0)
t.pendown()

# Draw the petals
for i in range(36):
    t.forward(100)
    t.left(170)

# Hide the turtle when finished
t.hideturtle()