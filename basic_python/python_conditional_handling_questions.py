"""
Take 3 numbers from user and find the largest number
among them
"""
greatest = 0
lowest = 0
low = 0
x, y, z = input("Enter three numbers ---> ").split(' ')
num1 = int(x) ; num2 = int(y); num3= int(z)
if( num1 > num2 and num1 > num3):
    greatest = num1
    if(num2 > num3):
        lowest = num3
    else:
        lowest = num2
elif(num2 > num1 and num2 > num3):
    greatest = num2
    if(num3 > num1):
      lowest  = num1
    else:
      lowest = num3
else:
    greatest = num3
    if(num1 < num2):
        lowest = num1
    else:
        lowest = num2

print("Greatest number is --->", \
      greatest,\
      "\nLowest number is ----> ", lowest)