# Create a program that asks for two numbers
# If the second number is not bigger than the first one it should print:
# "The second number should be bigger"
#
# If it is bigger it should count from the first number to the second by one
# 
# example:
#
# first number: 3, second number: 6, should print:
#
# 3
# 4
# 5

numberone = int(input('Enter number one: '))
numbertwo = int(input('Enter number two: '))

if numberone > numbertwo:
  print('The second number should be bigger')

if numberone < numbertwo:
  for i in range(numberone, numbertwo, 1):
    print(i)