"""
Create a method which will take input and verify
- if number is negative then display invalid value
- if number is zero, display zero
- if number is more than zero then check even or ODD
"""
def is_evn_or_odd(num):
    """
    Checks if the number is even or odd
    :param num:
    :return:
    """
    if(num == 0):
        print('number entered is 0')
    elif(num < 0):
        print("Invalid Value")
    elif(num % 2 == 0):
        print("even number")
    else:
        print("odd number")

##### main code #########
num = input("Enter any number ---> ")
is_evn_or_odd( int(num) )
