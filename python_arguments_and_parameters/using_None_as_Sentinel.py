#We can solve the problem in don't_Use_Mutable_Default_Argument by using None as the dafault argument instead of a
#mutable value
def populate_list(list_to_populate=None, length=1):
  if(list_to_populate is None):
      list_to_populate = []
  for num in range(length):
    list_to_populate.append(num)
  return list_to_populate


returned_list = populate_list(length=4)
print(returned_list)
returned_list = populate_list(length=6)
print(returned_list)
