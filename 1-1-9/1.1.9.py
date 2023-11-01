import turtle as trtl

him = 'himgif.gif'
trtl.shapes = [him]

trtl.register_shape('him.gif')
trtl.shape(trtl.shapes)



wn = trtl.Screen()
wn.mainloop()