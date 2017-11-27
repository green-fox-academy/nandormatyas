# Write a program that asks for a number.
# It would ask this many times to enter an integer,
# if all the integers are entered, it should print the sum and average of these
# integers like:
#
# Sum: 22, Average: 4.4


one = int(input(' give me five numbers: '))
two = int(input('2.'))
three = int(input('3.'))
four = int(input('4.'))
five = int(input('5.'))

summa = one + two + three + four + five
average = summa / 5

print('Sum: ', summa, 'Average: ', average)