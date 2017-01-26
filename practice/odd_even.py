#!/usr/local/bin/python3.6

# check if user input is odd or even
# return special case if divisble by 4
# allow 2 inputs separated by ', ' then determine if the first is divisible by the 2nd

while True:
    case1 = input('Please input a # or pair of numbers: ')
    if case1 is '':
        break
    elif case1.isdigit():
        if int(case1) % 4 is 0:
            print('Divisible by 4! Crazy!')
        elif int(case1) % 2 is 0:
            print('Divisible by 2.')
        else:
            print('Not evenly divisible by 2')
    else:
        if len(case1.split(', ')) is 1 or len(case1.split(', ')) > 2:
            print("Please follow the format of ', ' and only enter 2 numbers.")
        else:
            num = case1.split(', ')[0]
            check = case1.split(', ')[1]
            if num.isdigit() and check.isdigit():
                if int(num) % int(check) is 0:
                    print(num, 'is evenly divisible by', check)
                elif int(num) % int(check) is not 0:
                    print(num, 'is not evenly divisible by', check)
            else:
                print("Please use numbers separated by a ', '")
