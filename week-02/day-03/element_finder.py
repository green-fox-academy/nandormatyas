# Check if the list contains "7" if it contains print "Hoorray" otherwise print "Noooooo"

numbers = [1, 2, 3, 4, 5, 6, 8, 7];
found = 0

for i in numbers:
    if i == 7:
        found += 1
        
    else:
        continue

if found > 0:
    print('hooray')

else:
    print('Nooooo')