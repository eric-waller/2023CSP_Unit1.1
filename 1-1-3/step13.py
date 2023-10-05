import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)

# stem
painter.color("green")
painter.pensize(15)
painter.goto(0, -150)
painter.setheading(90)
painter.forward(100)
#  leaf
painter.setheading(270)
painter.circle(20, 120, 20)
painter.setheading(90)
painter.goto(0, -60)
# rest of stem
painter.forward(60)
painter.setheading(0)

# change pen
painter.penup()
painter.shape("circle")
painter.turtlesize(2)

# draw flower
painter.goto(20, 180)

for petal in range(18):
    painter.right(20)
    painter.forward(30)
    painter.color("darkorchid")
    rem = petal % 4
    if (rem == 1):
        painter.color("blue")
    painter.stamp()
    if (rem == 2):
        painter.color("darkorchid")
    painter.stamp()
    if (rem == 3):
        painter.color("blue")
    if (rem == 0):
        painter.color("red")
    painter.stamp()

wn = trtl.Screen()
wn.mainloop()