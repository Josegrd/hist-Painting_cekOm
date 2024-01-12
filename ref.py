
from turtle import *
from random import randint

timmy = Turtle()
timmy.shape("turtle")
colormode(255)
timmy.speed("fastest")


# MAKE SPHIROGRAPH USING TURTLE LIBS
def sphirograph:
    for i in range(1, 360, 5):
        timmy.color(randint(0, 255), randint(0, 255), randint(0, 255))
        timmy.circle(100)
        timmy.setheading(i)

# MAKE SQUARE USING TURTLE LIBS
def square():
        timmy.right(90)

# MAKE DASH LINE USING TURTLE LIBS
def dash_line():
    for i in range(10):
        timmy.pendown()
        timmy.forward(10)
        timmy.penup()
        timmy.forward(10)

# RANDOM DOTS USING TURTLE LIBS
def random_walk():
    timmy.pensize(10)
    timmy.speed("fastest")

    def direction():
        directChoice = [timmy.right, timmy.left]
        return directChoice[randint(0, 1)]

    count = 0
    while count < 51:
        count += 1
        if (timmy.xcor() >-300 and timmy.xcor() <300) and\
           (timmy.ycor() >-300 and timmy.ycor() <300):
            timmy.color(randint(0, 255), randint(0, 255), randint(0, 255))
            timmy.forward(randint(20, 50))
            direction()(90)

# MAKE Triagle++ USING TURTLE LIBS
def Triagle():
    radius = 360
    angleShape = 3

    while radius/4 != 1:
        current_radius = radius/angleShape
        timmy.color(randint(0, 255), randint(0, 255), randint(0, 255))
        for r in range(angleShape):
            timmy.forward(100)
            timmy.left(current_radius)
        angleShape += 1

screen = Screen()
screen.exitonclick()