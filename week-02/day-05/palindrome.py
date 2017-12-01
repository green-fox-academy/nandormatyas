''' Exercise

Create a function named create palindrome following your current language's style guide.
It should take a string, create a palindrome from it and then return it. '''

a = input('Give me a word to palindrome: ')


def palindrome(a):
    a = a + a[::-1]
    return a

print(palindrome(a))


