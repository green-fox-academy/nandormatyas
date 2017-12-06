from tkinter import *

root = Tk()

canvas = Canvas(root, width='300', height='300')
canvas.pack()

# reproduce this:
# [https://github.com/greenfox-academy/teaching-materials/blob/master/workshop/drawing/super-hexagon/r6.gif]

#hexagon = canvas.create_polygon()

class GUI(Canvas):
    '''inherits Canvas class (all Canvas methodes, attributes will be accessible)
       You can add your customized methods here.
    '''
    def __init__(self,master,*args,**kwargs):
        Canvas.__init__(self, master=master, *args, **kwargs)

polygon = GUI(root)
polygon.create_polygon([150,75,225,0,300,75,225,150],     outline='gray', 
            fill='gray', width=2)

polygon.pack()


root.mainloop()