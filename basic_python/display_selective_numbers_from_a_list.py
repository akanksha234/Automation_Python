"""
Given a list 11,22,33,44
Display only those numbers which are not a mulitple of 3, 5, or 7
"""
given_list = [11, 22, 33, 44, 55, 66, 77, 88, 99, 110]
for num in given_list:
    if(num % 5 == 0 or num % 3 == 0 or num % 7 == 0):
        continue
    print(num)

