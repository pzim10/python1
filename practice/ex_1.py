#!/usr/local/bin/python3.5

mylist = [0,1,2,3,4,5,6]
mylist[0] = 1
mylist[4:7] = [5,8,13]
newlist = mylist[::-1]
print(newlist)
