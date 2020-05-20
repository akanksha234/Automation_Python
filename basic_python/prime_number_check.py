"""
Checking if the number is prime or not after taking input from the user.
"""
import math


def is_prime(input_number):
    """
    Checks if a number is prime
    :param input_number:
    :return boolean value:
    """
    sqrt_input_number = int( math.sqrt(input_number) )
    is_prime_num = True
    for num in range(2, sqrt_input_number+1):
        if(input_number % num == 0):
            is_prime_num = False
            break
    return is_prime_num

print()
#Multiple line string can be enteres in """
myURL = """
        This is my Testing World.
        Website is : www.theTestingWorld.com
        Call - WhatsApp : +91-8700359954
        """
print("####################################################")
input_number = int( input("Enter the number for prime check -----> ") )
if( is_prime(input_number) ):
    print(f"Yes, {input_number} is a prime number")
else:
    print(f"Number is composite.")
print(myURL)
