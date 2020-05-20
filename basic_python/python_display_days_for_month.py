"""
Take an input month number from the user.
Write a condition to display number of days in the given month.
if month number is incorrect, display message like INCORRECT MONTH
For Feb month, you can display 28 days.
"""
year = 1700
month = 1
def is_leap_year(year) :
    """
    determines if the year passed is leap or not
    :param year:
    :return: boolean value
    """
    is_leap = False
    if( year % 4 == 0 and year % 100 != 0):
        is_leap = True
    elif(year % 400 == 0):
        is_leap = True
    return is_leap

def switcher_month(month, year):
    """
    returns the number of days of that month
    :param month:
    :return: integer (number of days of input month)
    """
    switch = {
        1 : 31,
        3 : 31,
        4 : 30,
        5 : 31,
        6 : 30,
        7 : 31,
        8 : 31,
        9 : 30,
        10 : 31,
        11 : 30,
        12 :31
    }
    if( is_leap_year(year) ):
        switch[2] = 29
    else:
        switch[2] = 28
    print(switch)
    return switch.get(month)


while True:
    try:
       year = input("Please enter year ---> ")
       month = input("Please enter month----> ")
       year = int(year)
       month = int(month)
       if(year < 1600):
           raise ValueError("Year should be greater than 1600.")
       if(month == 0 or month > 12):
           raise ValueError("month value cannot be zero")
       break
    except ValueError as ve:
        print(ve)


print("There are {} days in mentioned month".format(switcher_month( month, year)))