def copy_files(file1, file2):
    fopen1 = open(file1, 'r')
    fopen2 = open(file2, 'w')
    fread1 = fopen1.read()
    fopen2.write(fread1)

file1 = input('file1? ')
file2 = input('file2? ')

copy_files(file1,file2)
