import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
spider = trtl.Turtle()
# create spider body
spider.pensize(40)
spider.circle(20)
#configure spider legs
leg_limit = 8
leg_length = 80
angle = 360 / leg_limit
spider.pensize(5)
leg_num = 0
#draw spider legs
while (leg_num < leg_limit):
  if (leg_num < 4):
    spider.goto(0, 20)
    spider.setheading(0.5 * angle * leg_num - 35)
    spider.forward(leg_length)
  else:
    spider.goto(0, 20)
    spider.setheading(90 + 0.5 * angle * leg_num - 35)
    spider.forward(leg_length)
  leg_num = leg_num + 1

spider.pencolor("purple")
spider.penup()
spider.goto(20, 0)
spider.pensize(20)
spider.pendown()
spider.circle(10)

spider.penup()
spider.goto(-20, 0)
spider.pendown()
spider.circle(10)

spider.pencolor("black")
spider.penup()
spider.goto(23, 1)
spider.pendown()
spider.circle(2)

spider.penup()
spider.goto(-19, 1)
spider.pendown()
spider.circle(2)

spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()