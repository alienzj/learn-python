#!/usr/bin/env python3

import turtle
pen = turtle.Pen()
pen.speed(0)
pen.pencolor("red")
pen.fillcolor("yellow")
pen.begin_fill()
for j in range(144):
    for i in range(4):
        pen.forward(100)
        pen.left(90)
    pen.right(10)
pen.end_fill()
