from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/triangles/r5.png]

xstart = 0
ybottom = 300
ytop = 287
triangle_pieces = 21
move = 0
for i in range(0, 21):
    xfirst = xstart + 14
    xlast = xstart + 7
    for _ in range(triangle_pieces):
        triangle = canvas.create_polygon(xstart, ybottom, xfirst, ybottom, xlast, ytop, xstart, ybottom, fill= 'white', outline="black")
        xstart = xfirst
        xfirst += 14
        xlast += 14
    triangle_pieces -= 1 
    move += 7
    xstart = move
    ybottom -= 13
    ytop -= 13


root.mainloop()