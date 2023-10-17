import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
spider = trtl.Turtle()
# create spider body
spider.pensize(50)
spider.circle(25)
#configure spider legs
leg_limit = 8
leg_length = 80
angle = 360 / leg_limit
spider.pensize(5)
leg_num = 0
#draw spider legs
while (leg_num < leg_limit):
  if (leg_num < 4):
    spider.penup()
    spider.goto(0, 35)
    spider.setheading(0.3 * angle * leg_num - 35 + 180)
    spider.penup()
    spider.goto(0, -5)
    spider.pendown()
    spider.circle(100, 90)

  else:
    spider.penup()
    spider.goto(0, 35)
    spider.setheading( -1 * (90 + 0.3 * angle * leg_num - 15))
    spider.penup()
    spider.goto(0, -5)
    spider.pendown()
    spider.circle(100, -90)

  leg_num = leg_num + 1

spider.penup()
spider.goto(10,-20)
spider.pendown()
spider.pensize(40)
spider.circle(15)

spider.pencolor("purple")
spider.penup()
spider.goto(25, -15)
spider.pensize(20)
spider.pendown()
spider.circle(10)

spider.penup()
spider.goto(-15, -15)
spider.pendown()
spider.circle(10)

spider.pencolor("black")
spider.penup()
spider.goto(23, -8)
spider.pendown()
spider.circle(2)

spider.penup()
spider.goto(-19, -8)
spider.pendown()
spider.circle(2)

spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()