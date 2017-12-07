from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300', bg = 'yellow')
canvas.pack()


def rectangles(x1, y1, x2, y2):
    d = (x2 - x1) // 3
    
    horizontals = canvas.create_line(x1, y1 + d, x2, y2 - d * 2)
    horizontals = canvas.create_line(x1, y1 + d * 2, x2, y2 - d)
    verticals = canvas.create_line(x1 + d, y1, x2 - d * 2, y2)
    verticals = canvas.create_line(x1 + d * 2, y1, x2 - d, y2)
    if d < 10:
        return
    for i in range(3):
        for j in range(3):
            if (i + j) % 2 != 0:
                return rectangles(x1 + j * d, y1 + i * d, x1 + (j + 1) * d, y1 + (i + 1) * d)

rectangles(0,0,300,300)

''' def rectangles2():

    horizontals = canvas.create_line(0, 100 + 100//3, 300 // 3, 100 + 100// 3)
    horizontals = canvas.create_line(0, 200 - 100//3, 300 // 3, 200 - 100// 3)

    horizontals = canvas.create_line(100, 100//3, (300 // 3) * 2, 100// 3)
    horizontals = canvas.create_line(100, (100//3) * 2, (300 // 3) * 2, (100// 3) * 2)

    verticals = canvas.create_line(100 + 100 // 3 , 0, 100 + 100 // 3, 300 // 3)
    verticals = canvas.create_line(200 - 100 // 3, 0, 200 - 100 // 3, 300 // 3)

    verticals = canvas.create_line(100 // 3 , 100, 100 // 3, 200)
    verticals = canvas.create_line((100 // 3) * 2 , 100, (100 // 3) * 2, 200)



rectangles2() '''
root.mainloop() 