''' Create a function that takes two strings as a parameter
    Returns the starting index where the second one is starting in the first one
    Returns -1 if the second string is not in the first one

Example

    input: "this is what I'm searching in", "searching"
    output: 17
 '''
sentence ="this is what I'm searching in"
word = "searching"


def part_finder(s, w):
    
    for i in range(len(s)) :
        if s[i:i+len(w)] == w :
            return i
        #else:
    return -1

print(part_finder(sentence, word))

      
