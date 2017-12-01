''' Exercise

Create a function named is anagram following your current language's style guide.
It should take two strings and return a boolean value depending on whether its an anagram or not. '''

a = input('First word: ')
b = input('Second word: ')


def anagram(a, b):
    a = a.replace(" ", "").lower()
    b = b.replace(" ", "").lower()
    alis = list()
    blis = list()
    for i in a:
        alis.append(i)
    for j in b:
        blis.append(j)
    alis = sorted(alis)
    blis = sorted(blis)
    print(alis, blis)
    if alis == blis:
        return True
    else:
        return False



print(anagram(a, b))

