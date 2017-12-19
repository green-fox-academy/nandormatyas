class Character():

    def __init__(self, x=0, y=0, image=None):
        self.image = image
        self.x = x
        self.y = y

class Hero(Character):
    def __init__(self, x=0, y=0, image= None):
        super().__init__(x, y, image)
        self.image = "hero-down.png"

