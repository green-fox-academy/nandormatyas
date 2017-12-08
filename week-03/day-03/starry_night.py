from tkinter import *
from random import randint

root = Tk()

canvas = Canvas(root, width='1980', height='1080', bg = "black")
canvas.pack()

# draw the night sky:
# - The background should be black
# - The stars should be small squares
# - The stars should have random positions on the canvas
# - The stars should have random color (some shade of grey)
def rgbhex(r,g,b):

   return '#%02x%02x%02x' % (r, g, b)

for i in range(2000):
    starx = randint(10, 1970) 
    stary = randint(10, 1070)
    rgb = randint(10, 200)
    color = rgbhex(rgb,rgb,rgb)
    stars = canvas.create_rectangle(starx, stary, starx + 3, stary + 3, fill = color)


root.mainloop()