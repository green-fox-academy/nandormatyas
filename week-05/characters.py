from tkinter import *


root = Tk()

class Character():
    def __init__(self, x, y, image, status, canvas):
        self.x = x
        self.y = y
        self.image = PhotoImage(file=image)
        self.status = status
        self.canvas = canvas

    def draw_character(self):
        self.canvas.create_image(self.x, self.y, anchor=NW, image=self.image)
        

    #def move_up(self, x, y, image)

#character = Character(0,0,'hero-down.png', None)
#character.draw_character()


