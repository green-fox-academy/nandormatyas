
from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()
x= 0
y=0
total = 300
part = total // 3
def draw(x, y, total, part):
    square = canvas.create_rectangle(x, y, x + part, y + part, fill = 'yellow')
    total -= part

    if total > 0:
        return canvas.create_rectangle(x, y, x + part, y + part, fill = 'yellow')
    else:
        return draw(x, y + part, total + 2*part, part)
        


draw(x, y, total, part)
root-mainloop()