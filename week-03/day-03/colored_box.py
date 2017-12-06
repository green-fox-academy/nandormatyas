from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# draw a box that has different colored lines on each edge.
coloredBox = canvas.create_rectangle(25, 25, 150, 75, fill = "green" )
line1 = canvas.create_line(25, 25, 150, 25, fill = "yellow")
line2 = canvas.create_line(25, 25, 25, 75, fill = "blue")
line3 = canvas.create_line(25, 75, 150, 75, fill = "black")
line4 = canvas.create_line(150, 25, 150, 75, fill = "purple")

root.mainloop()