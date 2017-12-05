''' Find the part of int

    Create a function that takes a number and a list of numbers as a parameter
    Returns the indeces of the numbers in the list where the first number is part of
    Returns an empty list if the number is not part any of the numbers in the list

Example

    input: [1, 11, 34, 52, 61], 1
    output: [0, 1, 4]
 '''
inpu = [1, 11, 34, 52, 61]
find = 1
indices = list()

def findnumber(n, ln):
    found = list()
    for i in ln:
        if str(n) in str(i):
            found.append(i) 
    return found

found = findnumber(find, inpu)

indices = [inpu.index(j) for j in found]

print(indices)
#print(findnumber(find, inpu))
        

    



