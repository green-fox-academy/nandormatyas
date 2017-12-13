import random

class CAB():
    def __init__(self, number, guesses, state):
        self.number = number
        self.guesses = guesses
        self.state = state

    def generate_number(self):
        number = random.randint(1111,9999)