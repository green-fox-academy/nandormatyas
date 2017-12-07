# Given a string, compute recursively (no loops) a new string where all the
# lowercase 'x' chars have been changed to 'y' chars.

def xchanger(string):
    if string == '':
        return ''
    elif string[0] == 'x':
        return 'y' + xchanger(string[1:])
    return string[0] + xchanger(string[1:])

string = "axaxax defrxcxcxcxxxx"
print(xchanger(string))
