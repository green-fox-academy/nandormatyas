from tkinter import *
from map_draw import *
from characters import *

root = Tk()
canvas = Canvas(root, width='720', height='792')
canvas.pack()
floor = PhotoImage(file="floor.png")      
wall = PhotoImage(file="wall.png")      

the_map = Map(floor, wall)
the_map.draw_tiles(canvas)

#character = Character(0,0,'hero-down.png', None, canvas)
#character.draw_character()



root.mainloop()