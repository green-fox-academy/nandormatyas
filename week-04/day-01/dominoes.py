class Domino(object):
    def __init__(self, value_a, value_b):
        self.values = [value_a, value_b]

    def __repr__(self):
        return '[{}, {}]'.format(self.values[0], self.values[1])


def initialize_dominoes():
    dominoes = []
    dominoes.append(Domino(5, 2))
    dominoes.append(Domino(4, 6))
    dominoes.append(Domino(1, 5))
    dominoes.append(Domino(6, 7))
    dominoes.append(Domino(2 ,4))
    dominoes.append(Domino(7, 8))
    dominoes.append(Domino(8, 9))
    dominoes.append(Domino(10, 1))
    dominoes.append(Domino(9, 10))

    return dominoes
dominoes = initialize_dominoes()
sorted_dominoes = []

sorted_dominoes.append(dominoes[0])

index_sorted = 0
while len(sorted_dominoes) < len(dominoes):
    for i in range(len(dominoes)):
        if sorted_dominoes[index_sorted].values[1] == dominoes[i].values[0]:
            sorted_dominoes.append(dominoes[i])
            index_sorted += 1

print(sorted_dominoes)
