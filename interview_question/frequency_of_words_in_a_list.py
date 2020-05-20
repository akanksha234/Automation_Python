# Write your frequency_dictionary function here:
def frequency_dictionary(words):
    frequency_dict = {}
    for word in words:
      if word in frequency_dict.keys():
        frequency_dict[word] += 1
      else:
        frequency_dict[word] = 1
    return frequency_dict
# Uncomment these function calls to test your  function:
print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}