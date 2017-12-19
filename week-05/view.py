from tkinter import *
from PIL import ImageTk, Image
import numpy as np

root = Tk()
canvas = Canvas(root, width='720', height='792')
canvas.pack()
floor = ImageTk.PhotoImage(Image.open("floor.png")) 
wall = ImageTk.PhotoImage(Image.open("wall.png")) 
hero = ImageTk.PhotoImage(Image.open("hero-down.png"))


'''     for i in range(len(map_read)):
        for j in range(len(map_read[i])):
            if map_read[i][j] == '0':
                canvas.create_image(j*72, i*72, anchor=NW, image=floor)
            else:
                canvas.create_image(j*72, i*72, anchor=NW, image=wall)'''
def draw_map():
    map_source = open("map.txt")
    map_read = map_source.read()
    x = 0
    y = 0
    for digit in map_read:
        if digit == '0':
            canvas.create_image(x, y, anchor=NW, image=floor)
            x += 72
            if x == 720:
                y += 72
                x = 0
        elif digit == '1':
            canvas.create_image(x, y, anchor=NW, image=wall)         
            x += 72
            if x == 720:
                y += 72
                x = 0
def draw_hero(x, y, image):
    canvas.create_image(x, y, anchor=NW, image=image)

draw_map()


#view = Map()
#view.draw_map()
#view.draw_hero()
#root.mainloop()