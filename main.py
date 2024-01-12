from turtle import *
from random import randint

tim = Turtle()
tim.penup()
tim.hideturtle()
colormode(255)


# MAKE HIST pAINTING RANDOM COLOR
def hist:
    color_draft = [(245, 243, 238), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

    y_axis = -200
    for j in range(10):
        tim.setpos((-220, y_axis))
        for i in range(10):
            random_color_index = randint(0, len(color_draft)-1)
            tim.pendown()
            tim.dot(20, color_draft[random_color_index])
            tim.penup()
            tim.forward(50)
        y_axis += 50

    screen = Screen()
    screen.exitonclick()

# EXTRACT COLOR FROM IMAGE USING COLORGRAM LIBS
import colorgram
def extractColorFromImage:
    colors = colorgram.extract('image.jpg', 30)
    list_color =[]
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        list_color.append((r, g, b))
    print(list_color)