
def line_counter(x):
    try: 
        fopen = open(x)
        fname = fopen.read()
        print(fname)
        lines = 1
        for i in fname:
            if i == '\n':
                lines += 1
        print(lines )
        fopen.close()
    except:
        print(0)

x = input('TXT? ')
line_counter(x)

