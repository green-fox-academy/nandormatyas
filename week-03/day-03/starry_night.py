from tkinter import *
from random import randint

root = Tk()

canvas = Canvas(root, width='300', height='300', bg = "black")
canvas.pack()

# draw the night sky:
# - The background should be black
# - The stars should be small squares
# - The stars should have random positions on the canvas
# - The stars should have random color (some shade of grey)
def rgbhex(r,g,b):

   return '#%02x%02x%02x' % (r, g, b)

for i in range(30):
    starx = randint(10, 290) 
    stary = randint(10, 290)
    rgb = randint(10, 200)
    color = rgbhex(rgb,rgb,rgb)
    stars = canvas.create_rectangle(starx, stary, starx + 3, stary + 3, fill = color)


root.mainloop()