''' Find the substring in the list

    Create a function that takes a string and a list of string as a parameter
    Returns the index of the string in the list where the first string is part of
    Returns -1 if the string is not part any of the strings in the list

Example

    input: "ching", ["this", "is", "what", "I'm", "searching", "in"]
    output: 4
 '''
s =["this", "is", "what", "I'm", "searching", "in"]
w ="ching"


def match_susbtring(s, w):
    found = list()
    for i in s :
        if str(w) in str(i):
            found.append(i) 
    return found

found = match_susbtring(s, w)
indices = [s.index(j) for j in found]

print(indices, found)

#print(match_susbtring(s,w))