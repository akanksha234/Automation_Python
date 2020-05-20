"""
Take 2 input from
user and interchange variable value
"""
num1 = int ( input("Enter 1st number --> ") )
num2 = int (  input("Enter 2nd number--> ") )
print(f"num1 = {num1}\nnum2= {num2}")
num3 = num1
num1 = num2
num2 = num3
print("After exchange......")
print(f"num1 = {num1}\nnum2= {num2}")


