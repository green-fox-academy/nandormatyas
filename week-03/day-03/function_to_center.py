from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a line drawing function that takes 2 parameters:
# the x and y coordinates of the line's starting point
# and draws a line from that point to the center of the canvas.
# fill the canvas with lines from the edges, every 20 px, to the center.

def to_the_center(x, y):

    line = canvas.create_line(x, y, 150, 150)

x = 0
y = 0
for i in range(0, 301, 20):
    to_the_center(i, 0)
    to_the_center(i, 300)
for i in range(0, 301, 20):
    to_the_center(0, i)
    to_the_center(300, i)





root.mainloop()