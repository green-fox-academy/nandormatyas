from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/line-play/r1.png]

for i in range(0,300,20):

    line = canvas.create_line(300-i, 300, 0, 300-i)
    line2 = canvas.create_line(300-i, 0, 300, 300-i)


root.mainloop()