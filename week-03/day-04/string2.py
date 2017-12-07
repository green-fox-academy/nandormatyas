# Given a string, compute recursively a new string where all the 'x' chars have been removed.
def xremover(string):
    if string == '':
        return ''
    elif string[0] == 'x':
        return '' + xremover(string[1:])
    return string[0] + xremover(string[1:])

string = "axaxax defrxcxcxcxxxx"
print(xremover(string))

