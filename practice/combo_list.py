#!/usr/local/bin/python3.6
from random import randint
# create 2 lists, then 2 random lists, see what they have in common and print out that list

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
while True:
    end = input('[y or n]Generate new lists?')
    if end is 'n' or end is '':
        break
    a = []
    b = []
    c= []
    check = 0
    while check is not 7:
        check = randint(0,9)
        a.append(check)

    while check is not 2:
        check = randint(0,9)
        b.append(check)
    a.sort()
    b.sort()
    print(a)
    print(len(a))
    print(b)
    print(len(b))

    for i in a:
        if i in b:
            c.append(i)
    c.sort()
    print(c)
