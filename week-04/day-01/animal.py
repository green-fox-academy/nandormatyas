class Animal(object):
    def __init__(self, hunger, thirst):
        self.hunger = hunger
        self.thirst = thirst

        print(hunger, thirst)
    def eat(self, x):
        self.hunger -= x
    def drink(self):
        self.thirst -= 1
    def play(self):
        self.thirst += 1
        self.hunger += 1

lion = Animal(50,50)
lion.eat(3)
print(lion.hunger)

