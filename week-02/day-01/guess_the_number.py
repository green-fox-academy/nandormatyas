# Write a program that stores a number, and the user has to figure it out.
# The user can input guesses, after each guess the program would tell one
# of the following:
#
# The stored number is higher
# The stried number is lower
# You found the number: 8

x = 12

guess = int(input('Guess the number: '))

if guess < x:
  print('The stored number is higher')
elif guess > x:
  print('The stored number is lower')
elif guess == x:
  print('You found the number:',x)