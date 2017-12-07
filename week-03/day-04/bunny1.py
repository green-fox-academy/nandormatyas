# We have a number of bunnies and each bunny has two big floppy ears.
# We want to compute the total number of ears across all the bunnies recursively (without loops or multiplication).

def bunnies_ears(bunnies):
    if bunnies == 1:
        return 2
    else: 
        return (bunnies/bunnies)*2 + bunnies_ears(bunnies - 1) 

bunnies = int(input('bunnies? '))
print(bunnies_ears(bunnies))