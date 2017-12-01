''' What is Armstrong number?

    An Armstrong number is an n-digit number that is equal to the sum of the nth powers of its digits.

    Let's demonstrate this for a 4-digit number: 1634 is a 4-digit number, 
    raise each digit to the fourth power, and add: 1^4 + 6^4 + 3^4 + 4^4 = 1634, so it is an Armstrong number.
    For a 3-digit number: 153 is a 3-digit number, raise each digit to the third power, 
    and add: 1^3 + 5^3 + 3^3 = 153, so it is an Armstrong number.

Exercise

Write a simple program to check if a given number is an armstrong number. 
The program should ask for a number. E.g. if we type 371, the program should print out: The 371 is an Armstrong number. '''

gnum = input('What number should I check?: ')
digits = len(gnum)
workspace = list()
total = 0

for i in gnum:
    i = int(i)
    workspace.append(i)

for j in workspace:
    total += j ** digits

if int(total) == int(gnum):
    print('The', gnum, 'is an Armstrong number.')
else:
    print('The', gnum, 'is not an Armstrong number.')



#print(total)
