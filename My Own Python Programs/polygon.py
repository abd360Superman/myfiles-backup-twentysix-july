x = int(input('How many sides are there in the polygon?'))
y = 360/x
import turtle
t = turtle.Pen()
for a in range(0, x):
    t.forward(y)
    t.left(y)

