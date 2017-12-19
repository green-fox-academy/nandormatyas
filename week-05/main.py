from view import *
from model import *
from PIL import ImageTk, Image


draw_map()
hero = Hero()

hero.image = ImageTk.PhotoImage(Image.open("hero-down.png"))
draw_hero(0,0, hero.image)

map_source = open("map.txt")
map_tiles = map_source.readlines()

class Controller():
    def on_key_press(self, e):
        if e.keycode == 40 :
            hero.image = ImageTk.PhotoImage(Image.open("hero-down.png"))
            if hero.y + 72 <= 720 and map_tiles[(hero.y + 72)//72][hero.x//72] == '0':
                hero.y = hero.y + 72
        elif e.keycode == 38:
            hero.image = ImageTk.PhotoImage(Image.open("hero-up.png"))
            if hero.y - 72 >= 0 and map_tiles[(hero.y - 72)//72][hero.x//72] == '0':
                hero.y = hero.y - 72
        elif e.keycode == 37:
            hero.image = ImageTk.PhotoImage(Image.open("hero-left.png"))
            if hero.x - 72 >= 0 and map_tiles[hero.y//72][(hero.x - 72)//72] == '0':
                hero.x = hero.x - 72
        elif e.keycode == 39:
            hero.image = ImageTk.PhotoImage(Image.open("hero-right.png"))
            if hero.x + 72 < 720 and map_tiles[hero.y//72][(hero.x + 72)//72] == '0':
                hero.x = hero.x + 72
        draw_hero(hero.x, hero.y, hero.image)
canvas.bind("<KeyPress>", Controller().on_key_press)
canvas.pack()
canvas.focus_set()



root.mainloop()
#print(map_tiles)