
try:
    openfile = open('my-file.txt')
    openfile.read()
    print(openfile)
except:
    print('Unable to read file: my-file.txt')