
def line_counter(x):
    try: 
        fopen = open(x)
        fopen = fopen.read()
        print(fopen)
        lines = 1
        for i in fopen:
            if i == '\n':
                lines += 1
        print(lines )
    except:
        print(0)

x = input('TXT? ')
line_counter(x)
