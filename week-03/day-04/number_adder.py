# Write a recursive function that takes one parameter: n and adds numbers from 1 to n.

def adder(n):
    if n == 0:
        return 0
    else:
        print(n)
        return n + adder(n - 1)

n = int(input('Number? '))
print(adder(n))