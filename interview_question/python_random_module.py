# Import random below:
import random


# Create random_list below:
#make a list of 100 values with each value being random between 1 and 100
random_list = [ random.randint(1, 100) for random_num in range(101)]


# Create randomer_number below:
#pick out one random number from a given list
randomer_number = random.choice( random_list )


# Print randomer_number below:
print(randomer_number)
