# However, the parameters must be listed in this order:
# All named positional parameters
# An unpacked positional parameter (*args)
# All named keyword parameters
# An unpacked keyword parameter (**kwargs)
def remove(filename, *args, **kwargs):
  with open(filename) as file_obj:
    text = file_obj.read()
  for arg in args:
    text = text.replace(arg, "")
  for kwarg, replacement in kwargs.items():
    text = text.replace(kwarg, replacement)
  return text

print(remove("text.txt", "generous", "gallant", fond="amused by", Robin="Mr. Robin"))