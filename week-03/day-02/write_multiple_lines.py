def multiline_writer(path, word, number):
    fopen = open(path, 'w')
    fopen.write((word + "\n") * number)

path = input('file? ')
word = input('Word? ')
number = int(input('Lines? '))

multiline_writer(path, word, number)
