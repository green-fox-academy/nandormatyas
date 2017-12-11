class Station(object):
    gas_amount = 10000
    def refill(self):
        x = car.capacity
        Station.gas_amount -= x
        car.gas_amountc += x




class Car(object):

    def __init__(self, gas_amountc = 0, capacity = 100):
        self.gas_amountc = gas_amountc
        self.capacity = capacity

station = Station()
car = Car()
station.refill()
print(Station.gas_amount)
print(car.gas_amountc)