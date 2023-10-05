import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
painter.pensize(5)

# starting location of the tower
x = -200
y = -100

# height of tower and a counter for each floor
num_floors = 63

# iterate
for floor in range(num_floors):
    # set placement and color of turtle
    painter.penup()
    painter.color("gray")
    rem = floor % 6
    if (rem<2):
        painter.color("blue")
    if (rem>3):
        painter.color("green")
    rem = floor % 21
    if (rem == 0):
        x = x + 60
        y = 0

    painter.goto(x, y)
    y = y + 5
    # draw the floor
    painter.pendown()
    painter.forward(50)

wn = trtl.Screen()
wn.mainloop()