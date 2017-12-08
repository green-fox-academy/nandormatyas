try:
    fopen = open('my-file.txt', 'w')
    fopen.write('Nandi')
except:
    print('Unable to write file: my-file.txt')