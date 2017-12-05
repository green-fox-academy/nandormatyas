def reverse_lines(filename):
    fopen = open(filename)
    fread = fopen.readlines()
    ordered = " "
    for i in fread[::-1]:
        ordered += i
    print(ordered)
        

filename = input('File? ')
reverse_lines(filename) 

