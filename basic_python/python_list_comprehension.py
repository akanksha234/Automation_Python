"""
Finding squares by list comprehension
"""

nums = list(range(10))
#print(list(nums))

squares = [ num ** 2 for num in nums]
print(squares)


#Create a new list named add_ten that adds ten to every element in the list nums.
nums = [4, 8, 15, 16, 23, 42]
add_ten = [ num + 10 for num in nums]
print(add_ten)


#Create a list which contains the product of each sublist
nested_lists = [[4, 8], [15, 16], [23, 42]]
product = [ num1*num2  for num1,num2 in nested_lists]
print(product)

#list containing boolean values depending upon if first number is greater then the second
nested_lists = [[4, 8], [16, 15], [23, 42]]
greater_than = [True if num1 > num2 else False
for num1,num2 in nested_lists]
print(greater_than)

#list only the first number of each sublist
nested_lists = [[4, 8], [16, 15], [23, 42]]
first_only = [ num1 for num1,num2 in nested_lists]
print(first_only)

#forming a list of sums of two lists using zip method
a = [1.0, 2.0, 3.0]
b = [4.0, 5.0, 6.0]
sums = [ num1+ num2 for num1,num2 in zip(a,b)]
print(sums)

#find a/b of each memeber of the given lists
a = [1.0, 2.0, 3.0]
b = [4.0, 5.0, 6.0]
quotients = [num1/num2 for num1, num2 in zip(a,b)]
print(quotients)