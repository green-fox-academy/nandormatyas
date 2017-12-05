def reverse_lines(filename):
    fopen = open(filename)
    fread = fopen.read()
    decrypted = " "
    for i in fread[::-1]:
        decrypted += i
    print(decrypted)

filename = input('File? ')
reverse_lines(filename) 