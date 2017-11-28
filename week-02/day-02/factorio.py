# - Create a function called `factorio`
#   that returns it's input's factorial


def factorio():
  factor = 1
  number = int(input('What number to factor?: '))
  for i in range(1, number, 1):
    factor *= (i +1)
  print(factor)

factorio()