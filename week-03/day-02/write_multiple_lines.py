def multiline_writer(path, word, number):
    try:
        fopen = open(path, 'w')
        fopen.write((word + "\n") * number)
    except:
        print('unable to write file')
path = input('file? ')
word = input('Word? ')
number = int(input('Lines? '))

multiline_writer(path, word, number)
