from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/purple-steps/r3.png]

x1 = 0
y1 = 0
#x2 = x1 + 20
#y2 = y1 + 20
while (x1 + 20) <= 300:
    square = canvas.create_rectangle(x1, y1, x1 + 20, y1 +20, fill = "purple")
    x1 += 20
    y1 += 20



root.mainloop()