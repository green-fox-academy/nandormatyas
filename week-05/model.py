import random

class Character():

    def __init__(self, x=0, y=0, image=None):
        self.image = image
        self.x = x
        self.y = y

class Hero(Character):
    def __init__(self, x=0, y=0, image= None, HP = 1000):
        super().__init__(x, y, image)
        self.image = "hero-down.png"

class Monster(Character):
    def __init__(self, x=0, y=0, image = None, HP = 400):
        super().__init__(x, y, image)
        self.image = "skeleton.png"
        self.x = random.randint(0, 9)*72
        self.y = random.randint(0, 9)*72

class Boss(Character):
    def __init__(self, x=0, y=0, image = None, HP = 2000):
        super().__init__(x,y,image)
        self.image = "boss.png"
        self.x = random.randint(0, 9)*72
        self.y = random.randint(0, 9)*72

