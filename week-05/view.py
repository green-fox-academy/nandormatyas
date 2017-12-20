from tkinter import *
from PIL import ImageTk, Image
import random
import time

root = Tk()
canvas = Canvas(root, width='720', height='792')
canvas.pack()
floor = ImageTk.PhotoImage(Image.open("floor.png")) 
wall = ImageTk.PhotoImage(Image.open("wall.png")) 
hero = ImageTk.PhotoImage(Image.open("hero-down.png"))

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

def draw_monster(x, y, image):
    canvas.create_image(x, y, anchor=NW, image=image)

def draw_boss(x, y, image):
    canvas.create_image(x, y, anchor=NW, image=image)
    
monsters_ready = []
def place_monsters(monster_class, map_place):
    monster_on_map = 0
    while monster_on_map < 5:
        monster = monster_class
        if map_place[monster.y//72][monster.x//72] != '0' or monster in monsters_ready:
            continue
        else:
            monster.image = ImageTk.PhotoImage(Image.open("skeleton.png"))
            draw_monster(monster.x, monster.y, monster.image)
            monsters_ready.append(monster)
            monster_on_map += 1


''' def draw_map():
    map_source = open("map.txt")
    map_read = map_source.read()
    for i in range(len(map_read)):
        for j in range(len(map_read[i])):
            if map_read[i][j] == '0':
                canvas.create_image(j*72, i*72, anchor=NW, image=floor)
            else:
                canvas.create_image(j*72, i*72, anchor=NW, image=wall)'''
#view = Map()
#view.draw_map()
#view.draw_hero()
#root.mainloop()