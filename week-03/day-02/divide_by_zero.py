def divide_ten(x):
    try:
        y = 10 / x
        print(y)
    except:
        x = 0
        print('Fail') 

x = int(input('number?'))
divide_ten(x)
