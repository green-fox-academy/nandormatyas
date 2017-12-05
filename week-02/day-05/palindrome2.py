''' Exercise

Create a function named search palindrome following your current language's style guide.
It should take a string, search for palindromes that at least 3 characters long and return a list with the found palindromes. '''

#a = input('Give me a word to palindrome: ')
a = "dog goat dad duck doodle never"

def search_palindrome(a):
    pali = list()
    y = 3
    while y <= len(a):
        for l in range(0, len(a) -1, 1):
            x = a[l:l+y:1] 
            if x == x[::-1]:
                pali.append(x)
        y = y +1
            
    return pali
    
print(search_palindrome(a))
                
        





