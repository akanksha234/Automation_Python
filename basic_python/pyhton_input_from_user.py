#taking user's input
first_name = input("Please enter your name---> ")
print("Your name is ---> " + first_name)

#remember input always outputs a string, we will have to typecast it
age = int(input("Please input your age---> "))
age_after_10_years = age + 10
#you will have to typecast for concatenating with the string
print(" You will be " + str(age_after_10_years) + " old after 10 years")
