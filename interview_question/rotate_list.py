# rotate list
# no time/space requirements
# return "rotated" version of input list
#rotate a list in any direction depending upon the index       


def rotate(my_list, num_rotations, direction):
    length_list = len(my_list)
    #when the num_of_rotation is greater then the length and is a mulitple of length than list
    #will be as it is without any rotation, howver if not than the remainder will be the number of roatations
    #the lsit will rotate
    if(num_rotations >= length_list):
        num_rotations %= length_list

    if(direction == "forward"):
        for count in range(num_rotations):
            last_element = my_list[-1]
            for i in range(length_list-1, 0, -1):
                my_list[i] = my_list[i-1]
            my_list[0] = last_element

    elif(direction == "backward"):
        for count in range(num_rotations):
            first_element = my_list[0]
            for i in range(0, length_list-1):
                my_list[i] = my_list[i+1]
            my_list[-1] = first_element

    return my_list



#### TESTS SHOULD ALL BE TRUE ####
print("{0}\n should equal \n{1}\n {2}\n".format(rotate(['a', 'b', 'c', 'd', 'e', 'f'], 1, "forward"), \
                    ['f', 'a', 'b', 'c', 'd', 'e'], \
                    rotate(['a', 'b', 'c', 'd', 'e', 'f'], 1, "forward") == ['f', 'a', 'b', 'c', 'd', 'e']))

print("{0}\n should equal \n{1}\n {2}\n".format(rotate(['a', 'b', 'c', 'd', 'e', 'f'], 2, "forward"),\
                ['e', 'f', 'a', 'b', 'c', 'd'],\
                rotate(['a', 'b', 'c', 'd', 'e', 'f'], 2, "forward") == ['e', 'f', 'a', 'b', 'c', 'd']))

print("{0}\n should equal \n{1}\n {2}\n".format(rotate(['a', 'b', 'c', 'd', 'e', 'f'], 3, "forward"),\
                    ['d', 'e', 'f', 'a', 'b', 'c'],\
                    rotate(['a', 'b', 'c', 'd', 'e', 'f'], 3,"forward") == ['d', 'e', 'f', 'a', 'b', 'c']))

print("{0}\n should equal \n{1}\n {2}\n".format(rotate(['a', 'b', 'c', 'd', 'e', 'f'], 4, "forward"),\
                    ['c', 'd', 'e', 'f', 'a', 'b'], \
                    rotate(['a', 'b', 'c', 'd', 'e', 'f'], 4, "forward") == ['c', 'd', 'e', 'f', 'a', 'b']))


print("{0}\n should equal \n{1}\n {2}\n".format(rotate(['a', 'b', 'c', 'd', 'e', 'f'], 1, "backward"), \
                                                ['b', 'c', 'd', 'e', 'f', 'a'],\
                            rotate(['a', 'b', 'c', 'd', 'e', 'f'], 1, "backward") == ['b', 'c', 'd', 'e', 'f', 'a']))

print("{0}\n should equal \n{1}\n {2}\n".format(rotate(['a', 'b', 'c', 'd', 'e', 'f'], 2, "backward"),\
                                                ['c', 'd', 'e', 'f', 'a', 'b'],\
                            rotate(['a', 'b', 'c', 'd', 'e', 'f'], 2, "backward") == ['c', 'd', 'e', 'f', 'a', 'b']))

print("{0}\n should equal \n{1}\n {2}\n".format(rotate(['a', 'b', 'c', 'd', 'e', 'f'], 3, "backward"),\
                            ['d', 'e', 'f', 'a', 'b', 'c'],\
                         rotate(['a', 'b', 'c', 'd', 'e', 'f'], 3, "backward") == ['d', 'e', 'f', 'a', 'b', 'c']))

print("{0}\n should equal \n{1}\n {2}\n".format(rotate(['a', 'b', 'c', 'd', 'e', 'f'], 4, "backward"),\
                                                ['e', 'f', 'a', 'b', 'c', 'd'], \
                                                rotate(['a', 'b', 'c', 'd', 'e', 'f'], 4, "backward") == ['e', 'f', 'a', 'b', 'c', 'd']))