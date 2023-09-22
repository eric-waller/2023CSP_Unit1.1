# import the turtle module
import turtle
import turtle as trtl

# create the turtle object
painter = trtl.Turtle()

print("making a circle...")

# ask user for a color (such as red, green, blue, pink, purple)
color = input("What color should the circle be?")

# ask user for the radius of a circle
radius = float(input("How big should the radius of the circle be?"))

# draw a circle with the radius and line color entered by the user
painter.pencolor(color)
painter.fillcolor(color)
painter.begin_fill()
painter.circle(radius)
painter.end_fill()
# get the screen object and make it persist
wn = trtl.Screen()
wn.mainloop()