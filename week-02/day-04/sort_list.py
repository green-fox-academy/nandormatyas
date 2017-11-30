''' 
    Create a function that takes a list of numbers as parameter
    Returns a list where the elements are sorted in ascending numerical order
    Make a second boolean parameter, if it's true sort that list descending

Example

    input [34, 12, 24, 9, 5]
    output [5, 9, 12, 24, 34]
'''
inpu = [34, 12, 24, 9, 5]
sorte = [5, 9, 12, 24, 34]

def ascend_or_decend(l):
    
    if l == sorted(l):
        return sorted(l, reverse=True)

    else:
        return sorted(l)



print(ascend_or_decend(sorte))

