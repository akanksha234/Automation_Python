class Random:
    pass


random = Random()

random.sample_attri = "hi"
print(random.sample_attri)
print(hasattr(random, "fake_attri"))
print( getattr(random, "sample_attrii", "nope") )

##for every element in the given list check if element has attribute count
#if yes then print the number of s in that element
how_many_s = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for element in how_many_s:
  if( hasattr(element, "count")):
    print(element.count('s'))
