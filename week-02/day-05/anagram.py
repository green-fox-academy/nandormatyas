''' Exercise

Create a function named is anagram following your current language's style guide.
It should take two strings and return a boolean value depending on whether its an anagram or not. '''

a = input('First word: ')
b = input('Second word: ')

def anagram(a, b):
    
    if a == (b[::-1]):
        return True
    else:
        return False

print(anagram(a, b))

