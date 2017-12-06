from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a square drawing function that takes 1 parameter:
# the square size
# and draws a square of that size to the center of the canvas.
# draw 3 squares with that function.

def draw_square(size):
    x = 150 - size / 2
    y = 150 - size / 2
    square = canvas.create_rectangle(x, y, x + size, y + size)

size = int(input('Size? '))
draw_square(size)
root.mainloop()