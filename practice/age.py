#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.
name = input('What is your name? ')
while True:
    age = input('How old are you? ')
    if age.isdigit():
        print('You are: '+ age)
        print('In 100 years you will be', 100 + int(age))
    elif age is '':
        break
    else:
    	print('Please enter a number.')



#while True:
#      int_array= input('[d for done]Enter a digit: ');
#      if int_array.isdigit():
 #        x.append(int(int_array))
  #    elif int_array is 'd':
   #      break
  #    else:
  #       print('Please enter a number.')
  # if len(x) is not 0:
  #    x = sorted(x)
  #    print(x)
  #    xSum = sum(x)
