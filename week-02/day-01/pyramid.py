# Write a program that reads a number from the standard input, then draws a
# pyramid like this:
#
#
#    *
#   ***
#  *****
# *******
#
# The pyramid should have as many lines as the number was

pyramid = int(input('How long pyramid you want?: '))

space = " "
star = "*"
a = 0

for i in range(0, pyramid):
  print( space * (pyramid - i -1) + star * (2 * i + 1))


