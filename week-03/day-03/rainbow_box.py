from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a square drawing function that takes 2 parameters:
# the square size, and the fill color,
# and draws a square of that size and color to the center of the canvas.
# create a loop that fills the canvas with rainbow colored squares.

def size_and_color(size, color):
    x = 150 - size / 2
    y = 150 - size / 2

    square = canvas.create_rectangle(x, y, x + size, y + size, fill = color)
size = int(input('Size? '))
color = input('Color? ')
size_and_color(size, color)



root.mainloop()