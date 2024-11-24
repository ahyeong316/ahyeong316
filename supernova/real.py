import turtle

t=turtle.Turtle()


for i in range(4):
    t.forward(100)
    t.right(90)

t.rt(90)
t.penup()
t.fd(50)  
t.pendown()
t.color("blue")
t.pensize(2)
t.circle(50)

t.lt(90)
t.forward(100)
t.right(135)
t.fd(70)
t.rt(90)
t.fd(70)
