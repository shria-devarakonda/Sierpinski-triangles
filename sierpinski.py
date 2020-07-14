import turtle
t = turtle

turtle.speed(0)
turtle.bgcolor("red")

turtle.pencolor("white")

def sierpinski(l,d):
    if d>1:
        t.dot()
    if d == 0:
        t.stamp()
    else:
        t.forward(l)
        sierpinski(l/2,d-1)
        t.backward(l)
        t.left(120)
        t.forward(l)
        sierpinski(l / 2, d - 1)
        t.backward(l)
        t.left(120)
        t.forward(l)
        sierpinski(l / 2, d - 1)
        t.backward(l)
        t.left(120)

sierpinski(200, 5)
