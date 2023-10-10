import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
spider = trtl.Turtle()
# create spider body
spider.pensize(40)
spider.circle(20)
#configure spider legs
leg_limit = 8
leg_length = 70
angle = 360 / leg_limit
spider.pensize(5)
leg_num = 0
#draw spider legs
while (leg_num < leg_limit):
  spider.goto(0, 20)
  spider.setheading(angle * leg_num)
  spider.forward(leg_length)
  leg_num = leg_num + 1
spider.hideturtle()
wn = trtl.Screen()
wn.mainloop()