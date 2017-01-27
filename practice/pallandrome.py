#!/usr/local/bin/python3/6

# check if input is a pallandrome

while True:
    beg, end = '', ''
    word = input('Try and input a pallandrome: ')
    if word is '':
        break
    elif len(word) % 2 == 0:
        beg, end = word[0: len(word)//2 :1], word[-1: len(word)//2 - 1 :-1]
        print('First half: ' + beg)
        print('Second half: ' + end)
    elif len(word) % 2 == 1:
        beg, end = word[0: len(word)//2 + 1 :1], word[-1: len(word)//2 - 1 :-1]
        print('First half: ' + beg)
        print('Second half: ' + end)
    if beg == end:
        print("You found a pallandrome!")
