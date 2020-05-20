"""
Generate a random integer and form a list of them by list comprehension
"""
from random import randint
#We will form a list of 12 random integers which will range from that num to 2 times that number
random_integers = [ randint(1, 2* num) for num in range(1,12)]
print(random_integers)

single_digits = list(range(0,10))
squares = []
for digit in single_digits:
  print(digit)
  #squares = squares + [digit**2] or use below statement
  squares.append(digit**2)

print (squares)


#cubes using list comprehension
cubes = [ digit**3  for digit in single_digits]
print(cubes)