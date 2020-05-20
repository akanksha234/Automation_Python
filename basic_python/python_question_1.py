"""
Take Name, Age and Location from User

Print data in following format

User name is <NAME>, is <AGE> years old and lives in <LOCATION>
"""

name = input("Enter your name ---> ")
age = int ( input("How old are you? ---> ") )
location = ''
print("Please enter your address ---> ")
while input() != '':
    location += input()

print(f"User name is {name}, is {age} years old and lives at '{location}'")