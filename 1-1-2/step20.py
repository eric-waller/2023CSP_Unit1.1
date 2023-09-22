import turtle as trtl

painter = trtl.Turtle()

color = input("Benzene Ring Color:")

painter.pensize(5)
painter.pencolor(color)
painter.penup()
painter.goto(0, -100)
painter.pendown()
painter.circle(100, 360, 6)
painter.penup()
painter.goto(0, -70)
painter.pendown()
painter.circle(70, 360,)

wn = trtl.Screen()
wn.mainloop()
