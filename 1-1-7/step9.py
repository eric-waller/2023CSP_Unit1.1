#   a117_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic", "arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold", "red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  new_color = turtle_colors.pop()
  t.pencolor(new_color)
  t.fillcolor(new_color)
  my_turtles.append(t)

direction = 90
distance = 50
size = 1

#
startx = 0
starty = 0

#
for t in my_turtles:
  t.pensize(size)
  t.penup()
  t.goto(startx, starty)
  t.pendown()
  t.setheading(direction)
  t.right(45)
  t.forward(distance)
  direction = t.heading()
  distance = distance + 5
  size = size + 1



#
  startx = t.xcor()
  starty = t.ycor()

wn = trtl.Screen()
wn.mainloop()