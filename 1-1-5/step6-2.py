import turtle as trtl

screen_h = 400
screen_w = 420
startx = -100
starty = -100
turtle_scale = 1.5

def move():
  robot.dot(10)
  robot.fd(50)

def turn_left():
  robot.speed(0)
  robot.lt(90)
  robot.speed(2)

def turn_right():
  robot.speed(0)
  robot.right(90)
  robot.speed(2)

wn = trtl.Screen()
wn.setup(width=screen_w, height=screen_h)
robot_image = "robot.gif"
wn.addshape(robot_image)

robot = trtl.Turtle(shape=robot_image)
robot.hideturtle()
robot.color("darkorchid")
robot.pencolor("darkorchid")
robot.penup()
robot.setheading(90)
robot.turtlesize(turtle_scale, turtle_scale)
robot.goto(startx, starty)
robot.speed(2)
robot.showturtle()

wn.bgpic("maze2.png")

turn_right()
for step in range(2):
  for step in range(3):
    move()
  turn_left()
move()

robot.goto(startx, starty)

turn_right()
for step in range(3):
  move()
turn_right()
for step in range(2):
  move()


wn.mainloop()
