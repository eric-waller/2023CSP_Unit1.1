import turtle as trtl
wn = trtl.Screen()

shape = ["smallhim.gif"]
order = 0
him_gif = shape[order]

wn.register_shape(him_gif)

tyler = trtl.Turtle(shape = him_gif)

tyler.forward(20)

wn.mainloop()