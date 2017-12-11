class Sharpie(object):
    def __init__(self, color, width):
        self.color = color
        self.width = width
        self.ink_amount = 100

    def use(self, ink):
        self.ink_amount -= ink

sharpie = Sharpie("red", 100)

sharpie.use(30)
print(sharpie.ink_amount)
