#!/usr/local/bin/python3.6

# Return a list of numbers that divide evenly into (input)

while True:
    x = input('Choose a positive number: ')
    if x.isdigit():
        x = int(x)
        if x < 0:
            print('Please input a positive whole number.')
        elif x is 0:
            print('0')
        else:
            for i in range(1, x//2 + 2):
                if x % i is 0:
                    print(i)
            if x > 2:
                print(x)
    elif x is '':
        break
    else:
        print('Please input a real whole number')
