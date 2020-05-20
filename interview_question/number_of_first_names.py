"""
Create a function named count_first_letter that takes a dictionary named names as a parameter. names should be a dictionary where the key is a last name and the value is a list of first names. For example, the dictionary might look like this:

names = {"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}
The function should return a new dictionary where each key is the first letter of a last name, and the value is the number of people whose last name begins with that letter.

So in example above, the function would return:

{"S" : 4, "L": 3}

"""

# Write your count_first_letter function here:
def count_first_letter(my_dict):
  last_name_with_the_letter = {}
  for last_name, first_names in my_dict.items():
    first_char_last_name = last_name[0]
    if(first_char_last_name in last_name_with_the_letter):
         last_name_with_the_letter[first_char_last_name]+= len(first_names)
    else:
      last_name_with_the_letter[first_char_last_name] =len(first_names)

  return last_name_with_the_letter


# Uncomment these function calls to test your  function:
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}