#!/usr/bin/python3.4

import turtle

turtle.pensize(3)
turtle.penup()
turtle.goto(-200, -50)
turtle.pendown()
turtle.circle(40, steps = 3)

turtle.penup()
turtle.goto(-100, -50)
turtle.pendown()
turtle.circle(40, steps = 4)

turtle.penup()
turtle.goto(0, -50)
turtle.pendown()
turtle.circle(40, steps = 5)

turtle.penup()
turtle.goto(100, -50)
turtle.pendown()
turtle.circle(40, steps = 20)

turtle.penup()
turtle.goto(200, -50)
turtle.pendown()
turtle.circle(40)

turtle.done()
