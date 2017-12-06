from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/envelope-star/r2.png]

for i in range(0, 150, 10):
    line1 = canvas.create_line(150, i, 150 - i, 150)
    line2 = canvas.create_line(150, i, 150 + i, 150)
    line3 = canvas.create_line(150 - i, 150, 150, 300 - i)
    line4 = canvas.create_line(150 + i, 150, 150, 300 - i)



root.mainloop()