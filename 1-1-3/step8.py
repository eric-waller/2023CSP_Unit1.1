#   a113_forward_and_right.py
import turtle as trtl

painter = trtl.Turtle()

# Add code to make the turtle move forward 20 pixels
# and then turn right 20 degrees
painter.shape("circle")
for number in range(18):
    painter.stamp()
    painter.penup()
    painter.forward(20)
    painter.right(20)
    painter.pendown()

wn = trtl.Screen()
wn.mainloop()