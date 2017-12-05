try:
    fopen = open('my-file.txt', 'w')
    fopen.write('Nandi')
except:
    print('unable to write file: my-file.txt')