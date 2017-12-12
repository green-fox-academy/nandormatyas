class Aircraft():

    def __init__(self, ammo, max_ammo, base_damage, typo):
        self.ammo = ammo
        self.max_ammo = max_ammo
        self.base_damage = base_damage
        self.typo = typo
        self.ammo = 0
        if self.typo == 'F16':
            self.max_ammo = 8
            self.base_damage = 30
        elif self.typo == 'F35':
            self.max_ammo = 12
            self.base_damage = 50
    
    def fight(self):
        damage = self.ammo * self.base_damage
        self.ammo = 0
        return damage

    def refill(self, fillup):
        self.fillup = fillup
        for munition in range(fillup):
            while self.ammo < self.max_ammo and self.ammo < self.fillup:
                self.ammo += 1
        return fillup - self.ammo

    def getType(self):
        return self.typo


    def getStatus(self, typo = None):
        return 'Type: ' + str(self.typo) + ' Ammo: ' + str(self.ammo) + ' Base damage: ' + str(self.base_damage) + ' All damage: ' + str(self.ammo * self.base_damage) 


f35 = Aircraft(None, None, None, 'F35')
f16 = Aircraft(None, None, None, 'F16')

#print(f35.getType())
#f35.refill(100)
#f16.refill(4)
#print(f35.getStatus())
#print(f35.fight())
#print(f16.getStatus())

class Carrier():
    def __init__(self, aircrafts, base_ammo, health):
        self.aircrafts = aircrafts
        self.aircrafts = list()
        self.base_ammo = base_ammo
        self.health = health
        self.base_ammo = 4000
        self.health = 10000

    def addAircraft(self, craft):
        self.craft = Aircraft(None, None, None, craft)
        self.aircrafts.append(craft)

    def getStatus(self):
        #return 'HP: ' + str(self.health) + ' Aircraft count: ' + str(len(self.aircrafts)) + ' Ammo Storage: ' + str(self.base_ammo) + ' Total damage: '
        counter = 0
        while counter < len(self.aircrafts):
            for stored in self.aircrafts:
                stored = self.craft
                print(Aircraft.getStatus(stored))
                counter += 1

carrier = Carrier(None, None, None)
carrier.addAircraft('F16')
carrier.addAircraft('F16')
carrier.addAircraft('F35')

print(carrier.aircrafts)
print(carrier.getStatus())





