# import turtle module
import turtle as trtl

# create turtle object
painter = trtl.Turtle()

# set the pen and fill colors
painter.pensize(5)
painter.color("red")
painter.fillcolor("green")
# then draw a circle
painter.begin_fill()
painter.circle(60)
painter.end_fill()

# move the turtle to another part of the screen
painter.penup()
painter.goto(100, -140)
painter.pendown()
# change both the pen and fill colors
painter.pencolor("blue")
painter.fillcolor("orange")
# then draw a polygon of your choice
painter.begin_fill()
painter.circle(75, 360, 6)
painter.end_fill()
# create screen object and make it persist
wn = trtl.Screen()
wn.mainloop()