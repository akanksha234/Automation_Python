"""
Find factorial of a  given number
"""
def find_factorial(num):
    result = 1
    if (num == 0 or num == 1):
        return 1
    else:
        for i in range(num, 1,  -1):
            result *= i

    return result

##### main code ##################
num = int( input("Enter a number: ") )
factorial = find_factorial(num)
print(f"factorial of {num} is {factorial}")


