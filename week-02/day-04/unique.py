''' Create a function that takes a list of numbers as a parameter
    Returns a list of numbers where every number in the list occurs only once


    input: [1, 11, 34, 11, 52, 61, 1, 34]
    output: [1, 11, 34, 52, 61] '''

inpu = [1, 11, 34, 11, 52, 61, 1, 34]

def unique(l):

    out = list()
    for i in l:
        if i in out:
            continue
        else:
            out.append(i)
    return out

print(unique(inpu))



