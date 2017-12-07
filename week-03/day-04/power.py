# Given base and n that are both 1 or more, compute recursively (no loops)
# the value of base to the n power, so powerN(3, 2) is 9 (3 squared).

def to_the_power(base, power):
    if power < 1:
        return 1
    else:
        print(base, power)
        return base * to_the_power(base, power - 1)

base = int(input('base? '))
power = int(input('power? '))

print(to_the_power(base, power))

