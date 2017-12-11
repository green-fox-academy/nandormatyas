class Counter(object):
    def __init__(self, int_number = 0):
        self.int_number = int_number
    def add(self, number = 0):
        if number == 0:
            self.int_number += 1
            return self.int_number
        else:
            self.int_number += number
            return self.int_number
    
    def get(self):
        return self.int_number
    def reset(self):
        self.int_number = 0
        return self.int_number