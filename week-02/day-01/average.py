# Write a program that asks for 5 integers in a row,
# then it should print the sum and the average of these numbers like:
#
# Sum: 22, Average: 4.4

one = int(input(' give me five numbers: '))
two = int(input('2.'))
three = int(input('3.'))
four = int(input('4.'))
five = int(input('5.'))

summa = one + two + three + four + five
average = summa / 5

print('sum: ', summa, 'Average: ', average)