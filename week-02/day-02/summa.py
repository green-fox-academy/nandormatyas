# - Write a function called `sum` that sum all the numbers
#   until the given parameter

def sum():
  ranges = int(input('Sum until what number: '))
  total = 0
  for i in range(0, ranges, 1):
   # print(i)
    total += (i + 1)
  print(total)

sum()
