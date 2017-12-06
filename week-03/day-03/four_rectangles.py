from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# draw four different size and color rectangles.
box1 = canvas.create_rectangle(75, 75, 105, 105, fill = "green")
box2= canvas.create_rectangle(175, 175, 220, 250, fill = "blue")
box3 = canvas.create_rectangle(25, 250, 50, 260, fill = "yellow")
box4 = canvas.create_rectangle(145, 145, 155, 155, fill = "black")


root.mainloop()