"""
Program to write Great Fibonnaci Series
0 1 1 2 3 5 8 13
"""

def extract_fibbonaci_series(last_number):
    """
    This function gives you a fibonnaci list until the input number or the number less than the input number
    :param last_number:
    :return a list:
    """
    fibbonaci_list = [0, 1]
    index = 0
    next_num = -1
    while True:
        next_num = fibbonaci_list[index] + fibbonaci_list[index + 1]
        if(next_num >= last_number):
            break
        fibbonaci_list.insert(index + 2, next_num)
        index+=1
    return fibbonaci_list

###########main code#########################################################
num = int( input("Enter the number till which you want the fibonacci --> ") )
print("************************ FIBONACCI *****************************************\n",extract_fibbonaci_series(num))