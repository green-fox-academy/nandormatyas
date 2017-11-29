# Check if list contains all of the following elements: 4,8,12,16
# Create a function that accepts list_of_numbers as an input
# it should return "True" if it contains all, otherwise "False"

list_of_numbers = [2, 4, 6, 8, 10, 12, 14, 16]
x = [4,8,12,16,33]

def listnums(y):

    for i in x:
        if i in y:
            print(True)
        else:
            print(False)

listnums(list_of_numbers)

