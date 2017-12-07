from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# fill the canvas with a checkerboard pattern.
x = 0
y = 0
colors = ['black', 'white']
while x < 301 and y < 301:
    for color in colors:

        if color == colors[0]:
            color = colors[1]
            square = canvas.create_rectangle(x, y, x + 30, y + 30, fill = color)
            x += 30
        
            if x == 300:
                y += 30
                x = 0
                square = canvas.create_rectangle(x, y, x + 30, y + 30, fill = color)
                x += 30
        elif color == colors[1]:
            color = colors[0]
            square = canvas.create_rectangle(x, y, x + 30, y + 30, fill = color)
            x += 30
            
            if x == 300:
                y += 30
                x = 0
                square = canvas.create_rectangle(x, y, x + 30, y + 30, fill = color)
                x += 30
root.mainloop()