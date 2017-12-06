from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/purple-steps-3d/r4.png]

x = 0
y = 0
z = 20
while (x + z) < 300:
    square = canvas.create_rectangle(x, y, x + z, y + z, fill = "purple")
    x = x + z
    y = y + z
    z += 15

root.mainloop()