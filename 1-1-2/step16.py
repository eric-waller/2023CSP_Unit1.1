# import turtle module
import turtle as trtl

# create turtle object
painter = trtl.Turtle()

# add code here for a circle
painter.circle(25)

# move the turtle to another part of the screen
painter.penup()
painter.goto(50, 0)
painter.pendown()

# add code here for an arc
painter.circle(30, 180)

# move the turtle to another part of the screen
painter.penup()
painter.goto(-30, 20)
painter.pendown()

# add code here for an arc that is greater than 90 degrees and has 5 steps
painter.circle(15, 360, 5)

# move the turtle to another part of the screen
painter.penup()
painter.goto(-30, -50)
painter.pendown()

# add code here to create a polygon of your choice using the circle method
painter.circle(40, 360, 8)
# create screen object and make it persist
wn = trtl.Screen()
wn.mainloop()