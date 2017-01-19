#!/usr/local/bin/python3.5
##### PART 1 #####
#Accept user input, multiple times.
# Print the sum, minimum, maximum, median and average of the numbers
#(the median is the middle number in sorted order if the length of the
#list is odd; otherwise it is the average of the middle two numbers in sorted order)

#Git Comment
def part1():
   x= [];
   while True:
      int_array= input('[d for done]Enter a digit: ');
      if int_array.isdigit():
         x.append(int(int_array))
      elif int_array is 'd':
         break
      else:
         print('Please enter a number.')
   if len(x) is not 0:
      x = sorted(x)
      print(x)
      xSum = sum(x)
      xMin = min(x)
      xMax = max(x)
      xAvg = sum(x)/len(x)
   #   xIndex = len(x)//2
      if len(x) % 2 is 1:
         xMed = x[len(x)//2]
      else:
         xMed = (x[len(x)//2] + x[len(x)//2-1])/2
   #   print(xIndex)
      print('Sum:', xSum, end=' ')
      print('Min:', xMin, end=' ')
      print('Max:', xMax, end=' ')
      print('Avg:', xAvg, end=' ')
      print('Med:', xMed)

##### PART 2 ####

#Write a Stack class that uses a list for its internal data.
#It's easy to use a list as a stack by treating the end of the
#list as the top of the stack, and then using list's append and pop methods.
#Supply the user with push, pop, top, and size methods
#(your pop should return nothing: just remove the 'top' (last) element).
#Test by pushing the numbers 1 through 10, and then popping and printing them one at a time.

#Git comment
def part2():
   class Stack(list):
      def __init__(self):
         self.items = [];
      def push(self,y):
         self.items.append(y)
      def pop(self):
         self.items.pop()
      def top(self):
         return self.items[len(self.items)-1]
      def size(self):
         return len(self.items)
   newStk = Stack()
   for i in range(1,11):
      newStk.push(i)
      print(newStk.top())

   while newStk.size() > 1:
      newStk.pop()
      print(newStk.top())

##### PART 3 ####
# n + n

#Git comment
def part3():
   def num(n):
      z = 1
      if (n < 1):
         print('Not summable')
      for i in range(1,n+1):
         z += i
         print(z)

   while True:
      myNum = input('[q to quit]Input a number: ')
      if myNum.isdigit():
         num(int(myNum))
      elif myNum is 'q':
         break
      else:
         print("That isn't a number")


##### PART 4 ####
# part 4 sqrt function

#Git comment
def part4():
   def mySQRT(a,g):
      c = 1
      while True:
         b = g * g
         g2 = (g + a/g)/2
         if abs(g - g2) < 0.00005:
            return [c, g2]
         g = g2
         c += 1
   while True:
      check = input('[q to quit]Find the sqrt of: ')
      if check.isdigit():
         num = float(check)
         z = mySQRT(num,1.0)
         print(z)
      elif check is 'q':
         break
      else:
         print("Please enter a number to find it's sqrt")
bar = '#'
while True:
   print('\n' + bar*6 + ' MENU ' + bar*6 + '\n' + '[1] Part 1 (stats)' + '\n' + '[2] Part 2 (stack)' + '\n' + '[3] Part 3 (n += n)' + '\n' + '[4] Part 4 (sqrt)' + '\n' + '[5] Quit')
   menu = input('\nEnter an option to continue: ')
   if menu is '5':
      break
   options = {
      '1' : part1,
      '2' : part2,
      '3' : part3,
      '4' : part4,
   }
   options[menu]()
