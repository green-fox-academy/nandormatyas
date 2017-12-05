# Create a method that find the 5 most common lottery numbers otos.csv
def five_most_frequent(x):
    fopen = open(x)
    lines = fopen.readlines()
    numberslist = list()
    number_counter = dict()
    for line in lines:
        x = line.split('t')[4].strip()
        x = x.split(';')
        for i in x:
            if i.isdigit() is True:
                numberslist.append(i)
    for number in numberslist:
        number = int(number)
        if number in number_counter:
            number_counter[number] += 1
        else:
            number_counter[number] = 1
    orderdict = sorted(number_counter, key = number_counter.get, reverse = True)

    print(orderdict[:5])
x = 'otos.csv'
five_most_frequent(x)




