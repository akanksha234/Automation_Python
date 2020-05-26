#In python functions are objects
#e.g. code below

def add_five(num=3):
    return num + 5

print("###########first##############")
print(add_five)                             #prints the objects address
print(add_five(4))                           #invokes the function

#2. we can define functions within functions
def add_ten(num=2):

    def add_five(num):
        return num + 5

    num_plus_5 = add_five(num)
    return num_plus_5 + 5

print("##########second##############")
print( add_ten(20) )


#3 Returning functions from function
def get_math_function(operation):

    def add(num1, num2):
        return num1 + num2

    def subtract(num1, num2):
        return abs(num1 - num2)

    if(operation == '+'):
        return add
    elif (operation == '-'):
        return subtract

add_function = get_math_function('+')
sum = add_function(2, 3)

subtract_function = get_math_function('-')
difference = subtract_function(10, 50)

print('#############third##################')
print("sum = {},  difference = {}".format(sum, difference))


print("######################fourth####################")
#4. Decorating a function
#decorator is a function which will take a function and do some functionality around it
#sample function which prints my name
def question_decorator(print_name_func):

    def wrapper_function(*args, **kwargs):
        print("Hey!! who are you?")
        print_name_func(*args, **kwargs)
        print("Hey!! {name} I fuff you!! <3 <3 <3".format(name=args[0]))

    return wrapper_function


@question_decorator
def print_my_name(*args, **kwargs):
    print("Hi!! my name is {name}. I am {age} years old Nice to meet you :) ".format(name=args[0], age= args[1]))



# @question_decorator
# def print_Apoos_name():
#     print("Hi!! my name is Apoorav. Nice to meet you :) ")

# print_conversation = question_decorator(print_my_name)
# print_conversation()
print_my_name("Apoo", 25,'sexy','fandu')
print_my_name("akanksha", 25)


