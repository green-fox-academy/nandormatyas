students = [
        {'name': 'Rezso', 'age': 9.5, 'candies': 2},
        {'name': 'Gerzson', 'age': 10, 'candies': 1},
        {'name': 'Aurel', 'age': 7, 'candies': 3},
        {'name': 'Zsombor', 'age': 12, 'candies': 5}
]

# create a function that takes a list of students and prints:
# - Who has got more candies than 4 candies

# create a function that takes a list of students and prints: 
#  - how many candies they have on average

def morecandies():

    for i in students:
        x = i.get('candies')
        x = int(x)
        y = i.get('name')
        if x < 4:
            print(y)

morecandies()

def averagecandies():
    count = 0
    total = 0
    for i in students:
        x = i.get('candies')
        x = int(x)
        total += x
        count += 1
    print(total / count)

averagecandies()
