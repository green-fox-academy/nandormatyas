# Given a string, compute recursively a new string where all the
# adjacent chars are now separated by a "*".

def stargiver(string):
    if string == '':
        return ''
    else:
        return string[0] + '*' + stargiver(string[1:])

string = "axaxax defrxcxcxcxxxx"
print(stargiver(string))
