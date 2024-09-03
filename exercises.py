#Excercise 1
name=input('Enter your name:\n')
print('Welcome'+' '+ name)

#Excercise 2
hours=float(input('Enter hours:\n'))
rate=float(input('Enter rate:\n'))

pay=hours*rate

print('The pay is ', pay)

#Exercise 3
width=17
height=12.0


ans=width//2 #floor division rounds off the decimal to the nearest whole number
print(ans)

ans=width/2.0
print(ans)

ans=height/3
print(ans)

ans=1+2*5
print(ans)
#Exercise 4

#prompt the user to enter the temperature in celcius
celcius=input('Enter the  temperature in Celcius:\n')

#formula for converting celcius to fahrenheit
Fahrenheit=(9/5*celcius)+32

#prints result
print(Fahrenheit)
