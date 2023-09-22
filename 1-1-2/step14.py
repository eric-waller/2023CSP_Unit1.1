# import turtle module
import turtle as trtl

# create turtle object
painter = trtl.Turtle()
painter.pensize(5)

# move turtle without marking a line
painter.penup()
painter.goto(0, -20)
painter.pendown()

# draw a semi-circle
painter.circle(100, 180)

# move turtle without marking a line
painter.penup()
painter.goto(0, 20)
painter.pendown()

# draw a 3-step semi-circle
painter.circle(100, 180, 3)
painter.penup()
painter.goto(50, 0)
painter.pendown()
painter.circle(50, 135, 3)
painter.penup()
painter.goto(-50, 0)
painter.pendown()
painter.circle(50, 270, 5)

# create screen object and make it persist
wn = trtl.Screen()
wn.mainloop()