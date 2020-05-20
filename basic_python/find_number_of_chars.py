"""
Given a string,
Find the number of characters in that string, in this case 'a'
"""

sample_string = "aldksjfisdhaklhhd;klh;HJalldalkflaalkfhalfjbhgujabjkaabaaadf;kgjdkfg"
original_length = len(sample_string)
new_length = len( sample_string.replace('a',''))
frequency_of_a = original_length - new_length
print(f"a is present {frequency_of_a} times in the {sample_string}")

list1 = [1, 2, 3, 4]
list2 = ["akanksha", "raju"]
list3=[0]
print(list(zip(list1, list2, list3)))
#list1.append(list2)
list1.extend(list2)
print( list1 )

suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']

beginning = suitcase[0:4]
middle_index = int( len(suitcase)/2 - 1 )
middle = suitcase[middle_index : (middle_index+2)]
print(middle_index)
print(beginning)
print(middle)
suitcase.pop(1)
print(suitcase)

