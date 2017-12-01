''' exercise

Write a function to solve Josephus Problem. The program should ask for a number,
 this number represents how many people are in the "game".
 The return value should be the number of the "winning" seat. '''

peoplesum = int(input('How many people are there?: '))
peoplesum = list(range(1, peoplesum + 1))

idx = 1


while len(peoplesum) > 1:
    peoplesum.pop(idx)
    idx = (idx + 1) % len(peoplesum)
    
print(peoplesum)