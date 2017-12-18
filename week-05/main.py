from tkinter import *
from map_draw import *
from characters import *
from PIL import ImageTk, Image

root = Tk()
canvas = Canvas(root, width='720', height='792')
canvas.pack()
floor = ImageTk.PhotoImage(Image.open("floor.png")) 
wall = ImageTk.PhotoImage(Image.open("wall.png"))  

the_map = Map(floor, wall)
the_map.draw_tiles(canvas)

#character = Character(0,0,'hero-down.png', None, canvas)
#character.draw_character()



root.mainloop()