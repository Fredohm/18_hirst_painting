from turtle import Turtle, Screen
from random import choice

color_list = [(61, 48, 62), (221, 173, 192), (96, 104, 168), (141, 169, 165), (185, 96, 80), (170, 189, 221)]


def set_initial_position():
    turtle.hideturtle()
    turtle.penup()
    turtle.setheading(225)
    turtle.forward(500)


def draw_line_of_dots():
    for _ in range(10):
        turtle.setheading(0)
        turtle.dot(30, choice(color_list))
        turtle.forward(80)


def go_to_next_line():
    turtle.setheading(180)
    turtle.forward(800)
    turtle.setheading(90)
    turtle.forward(80)
    turtle.setheading(0)


turtle = Turtle()
turtle.speed("fastest")
screen = Screen()
screen.colormode(255)

set_initial_position()
for _ in range(10):
    draw_line_of_dots()
    go_to_next_line()

screen.exitonclick()


