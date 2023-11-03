import turtle as trtl
wn = trtl.Screen()

shape = ["smallhim.gif"]
him_gif = shape[0]
wn.register_shape(him_gif)

tyler = trtl.Turtle(shape = him_gif)

tyler.forward(20)

wn.mainloop()