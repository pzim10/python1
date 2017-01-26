#!/usr/local/bin/python3.6

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
print(a[:5])
while True:
    num = input('Input a number between 0 and 100:')
    if num is '':
        break
    if num.isdigit():
        top = int(num)
        for i in a:
            if top > i:
                b.append(i)
    
    print(b)
    b = []
