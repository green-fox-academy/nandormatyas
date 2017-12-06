from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# create a function that takes 1 parameter:
# a list of [x, y] points
# and connects them with green lines.
# connect these to get a box: [[10, 10], [290,  10], [290, 290], [10, 290]]
# connect these: [[50, 100], [70, 70], [80, 90], [90, 90], [100, 70],
# [120, 100], [85, 130], [50, 100]]
lists = [[10, 10], [290,  10], [290, 290], [10, 290]]
lists2 = [[50, 100], [70, 70], [80, 90], [90, 90], [100, 70], [120, 100], [85, 130], [50, 100]]
def connecter(lists):

    x = lists[0][0]
    y = lists[0][1]
    for i in lists:
        line = canvas.create_line(x, y, i[0], i[1])
        x = i[0]
        y = i[1]
    line = canvas.create_line(x, y, lists[0][0], lists[0][1])
connecter(lists2)
root.mainloop()