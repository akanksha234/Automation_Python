#Write your lambda function here
long_string  = lambda str : True if len(str) > 12 else False

print(long_string("short"))
print(long_string("photosynthesis"))

#Create a lambda function named double_or_zero that
#takes an integer named num. If num is greater than 10, return double num. Otherwise, return 0
double_or_zero = lambda num : num*2 if num > 10 else 0

print (double_or_zero(15))
print (double_or_zero(5))