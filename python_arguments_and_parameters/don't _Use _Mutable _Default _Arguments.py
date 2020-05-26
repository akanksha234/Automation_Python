#note that the default argument should be immutable as the mutable value have chance of retaining
#or withholding the previous arguments.
# #e.g.
#  Let’s say you have a function called populate_list that has two required arguments,
#  but it’s easy to see that we might want to give it some default arguments in case we don’t have either
#  list_to_populate or length every time. So we’d give it these defaults:
#
def populate_list(list_to_populate=[], length=1):
  for num in range(length):
    list_to_populate.append(num)
  return list_to_populate
# It’s reasonable to believe that list_to_populate will be given an empty list every time it’s called.
# This isn’t the case! list_to_populate will be given a new list once, in its definition, and all
# subsequent function calls will modify the same list. This will happen:
#
returned_list = populate_list(length=4)
print(returned_list)
returned_list = populate_list(length=6)
print(returned_list)
# # Prints [0, 1, 2, 3] -- this is expected
#
# print(returned_list)
# # Prints [0, 1, 2, 3, 0, 1, 2, 3, 4, 5] -- this is a surprise!



# When we call populate_list a second time we’d expect the list [0, 1, 2, 3, 4, 5].
# But the same list is used both times the function is called, causing some side-effects from
# the first function call to creep into the second. This is because a list is a mutable object.
#
# A mutable object refers to various data structures in Python that are intended to be mutated, or changed.
# A list has append and remove operations that change the nature of a list.
# Sets and dictionaries are two other mutable objects in Python.

