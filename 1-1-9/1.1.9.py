import turtle as trtl

trtl1 = trtl.Turtle()

trtles = [trtl, trtl1]

trtl.speed(10)

trtl1.speed(10)

redvalue = 0

greenvalue = 0

bluevalue = 0

wrmhle = []

rad = 0.05

fwd = 0.05

numnum = ["i", "i", "i", "i", "i", "i", "i", "i", "i", "i"]

for num in numnum:
    wrmhle.append(slice)

    wrmhle.append(slice)

trtl.left(45)

for sclice in wrmhle:
    trtl.color = (redvalue, greenvalue, bluevalue)

    trtl.circle(rad)

    rad *= 1.5

    redvalue += 5

    greenvalue += 5

    bluevalue += 5

    trtl.penup()

    trtl.forward(fwd)

    trtl.pendown()

    fwd *= 1.5

redvalue = 0

greenvalue = 0

bluevalue = 0

rad = 0.05

fwd = 0.05

trtl1.right(145)

for sclice in wrmhle:
    trtl1.color = (redvalue, greenvalue, bluevalue)

    trtl1.circle(rad)

    rad *= 1.5

    redvalue += 5

    greenvalue += 5

    bluevalue += 5

    trtl1.penup()

    trtl1.forward(fwd)

    trtl1.pendown()

    fwd *= 1.5

print(wrmhle)

print(numnum)

wn = trtl.Screen()

wn.mainloop