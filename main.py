import colorgram
from turtle import Turtle, Screen
from random import choice

# selected_colors = colorgram.extract('hirst-white-paper.jpg', 30)
# rgb_tuples = []
# for selected_color in selected_colors:
#     rgb_tuples.append(tuple(selected_color.rgb))
# print(rgb_tuples)

color_list = [(61, 48, 62), (221, 173, 192), (96, 104, 168), (141, 169, 165), (185, 96, 80), (170, 189, 221)]


def set_initial_position():
    turtle.hideturtle()
    turtle.penup()
    turtle.setheading(180)
    turtle.forward(360)
    turtle.setheading(270)
    turtle.forward(380)


def draw_point():
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()


def draw_line_of_points():
    for _ in range(10):
        turtle.setheading(0)
        turtle.pendown()
        turtle.color(choice(color_list))
        draw_point()
        turtle.penup()
        turtle.forward(80)


def go_to_next_line():
    turtle.setheading(180)
    turtle.forward(800)
    turtle.setheading(90)
    turtle.forward(80)
    turtle.setheading(0)
    print(turtle.pos())


turtle = Turtle()
turtle.speed("fastest")
screen = Screen()
screen.colormode(255)

set_initial_position()
for _ in range(10):
    draw_line_of_points()
    go_to_next_line()

screen.exitonclick()


