from tkinter import *


root = Tk()
canvas = Canvas(root, width="720", height="792")
canvas.pack()

class Character():
    def __init__(self, x, y, status, image, canvas):
        self.x = x
        self.y = y
        self.image = image
        self.status = status
        self.canvas = canvas

    def draw_character(self):
        self.canvas.create_image(self.x, self.y, anchor=NW, image=self.image)
        

    def on_key_press(self, e):
        if e.keycode == 40 :
            self.image = PhotoImage(file="hero-down.png")
            if character.y + 72 <= 720:
                character.y = character.y + 72
        elif e.keycode == 38:
            self.image = PhotoImage(file="hero-up.png")
            if character.y - 72 >= 0:
                character.y = character.y - 72
        elif e.keycode == 37:
            self.image = PhotoImage(file="hero-left.png")
            if character.x - 72 >= 0:
                character.x = character.x - 72
        elif e.keycode == 39:
            self.image = PhotoImage(file="hero-right.png")
            if character.x + 72 < 720:
                character.x = character.x + 72
        character.draw_character()

character = Character(0,0,None, None, canvas)
character.draw_character()
canvas.bind("<KeyPress>", character.on_key_press)
canvas.pack()

# Select the canvas to be in focused so it actually recieves the key hittings
canvas.focus_set()

# Draw the box in the initial position
character.draw_character()

root.mainloop()
