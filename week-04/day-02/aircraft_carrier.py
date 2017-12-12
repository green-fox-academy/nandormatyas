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
                if self.fillup != 0:
                    self.ammo += 1
                    fillup -= 1
        return self.fillup

    def getType(self):
        return self.typo


    def getStatus(self, typo = None):
        return 'Type: ' + self.typo + ' Ammo: ' + str(self.ammo) + ' Base damage: ' + str(self.base_damage) + ' All damage: ' + str(self.ammo * self.base_damage) 


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
        self.base_ammo = 3000
        self.health = 10000

    def addAircraft(self, craft):
        self.craft = Aircraft(None, None, None, craft)
        self.aircrafts.append(self.craft)
    
    def fill_aircraft(self, base_ammo=None):
        Carrier.base_ammo = self.base_ammo
        ammo_need = 0
        for x in range(len(self.aircrafts)):
            need = self.aircrafts[x].max_ammo
            ammo_need += need 
        if ammo_need < self.base_ammo:
            for i in range(len(self.aircrafts)):
                while self.aircrafts[i].ammo < self.aircrafts[i].max_ammo and self.base_ammo != 0:
                        self.aircrafts[i].ammo += 1
                        self.base_ammo -= 1
        elif self.base_ammo <= 0:
            print('No ammo left')
        else:
            order = self.aircrafts
            while self.base_ammo != 0:
                for i in range(len(order)):
                    if order[i].typo == 'F35':
                        while order[i].ammo < order[i].max_ammo and self.base_ammo != 0:
                                order[i].ammo += 1
                                self.base_ammo -= 1
                for i in range(len(self.aircrafts)):
                    while self.aircrafts[i].ammo < self.aircrafts[i].max_ammo and self.base_ammo != 0:
                        self.aircrafts[i].ammo += 1
                        self.base_ammo -= 1

    def fight(self, carrier):
        damage = 0
        for i in range(len(self.aircrafts)):
           fire = self.aircrafts[i].ammo * self.aircrafts[i].base_damage
           damage += fire
           self.aircrafts[i].ammo = 0
           carrier.health -= fire

    def getStatus(self):
        total_damage = 0
        for i in range(len(self.aircrafts)):
            damages = self.aircrafts[i].ammo * self.aircrafts[i].base_damage
            total_damage += damages
        print('HP: ' + str(self.health) + ' Aircraft count: ' + str(len(self.aircrafts)) + ' Ammo Storage: ' + str(self.base_ammo) + ' Total damage: ' + str(total_damage))
        counter = 0
        while counter < len(self.aircrafts):
            for stored in self.aircrafts:
                print(Aircraft.getStatus(stored))
                counter += 1

carrier = Carrier(None, None, None)

carrier.addAircraft('F16')
carrier.addAircraft('F16')
carrier.addAircraft('F35')
carrier.addAircraft('F16')
carrier.addAircraft('F35')

#print(carrier.aircrafts)
carrier.fill_aircraft()
carrier.getStatus()
class Carrier2():
    def __init__(self, aircrafts, base_ammo, health):
        self.base_ammo = base_ammo
        self.health = health
        self.base_ammo = 4000
        self.health = 10000

carrier2 = Carrier2(None, None, None)
carrier.fight(carrier2)
print(carrier2.health)
carrier.getStatus()






