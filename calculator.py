#User inputs a number
n1=int(input('Enter the First Number:\n'))
n2=int(input('Enter the Second Number:\n'))

#User chooses an arithmetic expression from the list
number=int(input('Choose an Arithmetic Expression:\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n'))

#if user chooses 1, the numbers are added
if number == 1:
 sum=n1+n2
 print(sum)

#if user chooses 2, the numbers are subtracted

elif number == 2:
 sum=n1-n2
 print(sum)

#if user chooses 3, the numbers are multiplied

elif number == 3:
 sum=n1*n2
 print(sum)

#if user chooses 4, num1 is divided by num
else:
 sum=n1/n2
 print(sum)



