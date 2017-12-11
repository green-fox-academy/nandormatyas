class Station(object):
    gas_amount = 10000
    def refill(self, Car):
        x = car.capacity
        self.gas_amount -= x
        car.gas_amountc += x




class Car(object):

    def __init__(self, gas_amountc = 0, capacity = 100):
        self.gas_amountc = gas_amountc
        self.capacity = capacity

Station()
car = Car()

print(Station.gas_amount)
#print(Car.gas_amountc)