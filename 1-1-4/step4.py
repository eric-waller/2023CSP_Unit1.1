import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
painter.color("green")

line = 1
# Add a loop with a zero-iteration condition
while (line % 2 == 2):
    painter.color("red")

# Add an infinite loop
while (line % 2 != 2):
    painter.forward(50)
    painter.right(92)
    line = line + 1


wn = trtl.Screen()
wn.mainloop()