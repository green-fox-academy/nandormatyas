from tkinter import *
#from characters import *


root = Tk()
canvas = Canvas(root, width='720', height='792')
canvas.pack()

class Map(object): 
    def __init__(self, accessable_tile, not_accessabla_tile):
        self.map_source = open('map.txt')
        self.map_read = self.map_source.read()
        #self.accessable_tile = accessable_tile
        #self.not_accessabla_tile = not_accessabla_tile  
        self.accessable_tile = PhotoImage(file="floor.png")      
        self.not_accessabla_tile = PhotoImage(file="wall.png")      



    def draw_tiles(self, canvas):
        self.canvas = canvas
        x = 0
        y = 0
        for digit in self.map_read:
            if digit == '0':
                self.canvas.create_image(x, y, anchor=NW, image=self.accessable_tile)
                x += 72
                if x == 720:
                    y += 72
                    x = 0
            elif digit == '1':
                self.canvas.create_image(x, y, anchor=NW, image=self.not_accessabla_tile)
                x += 72
                if x == 720:
                    y += 72
                    x = 0
the_map = Map(None, None)
the_map.draw_tiles(canvas)

root.mainloop()
