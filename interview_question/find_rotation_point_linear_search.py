# find rotation point
# No time/space requirements
# return index of "rotation point" element
#given a sorted list rotated k times, return the index where the “unrotated” list should begin.
#e.g. rotated_list = ['c', 'd', 'e', 'f', 'a']
# rotation_point(rotated_list)
# index 4
# a sorted list would start with 'a'


def rotation_point(rotated_list):
    shortest = rotated_list[0]
    position_of_shortest = 0
    for index in range(1, len(rotated_list)):
        if(not shortest < rotated_list[index]):
            shortest = rotated_list[index]
            position_of_shortest = index
    return position_of_shortest


#### TESTS SHOULD ALL BE TRUE ####
print("{0}\n should equal \n{1}\n {2}\n".format(rotation_point(['a', 'b', 'c', 'd', 'e', 'f'])\
                                                , 0, rotation_point(['a', 'b', 'c', 'd', 'e', 'f']) == 0))

print("{0}\n should equal \n{1}\n {2}\n".format(rotation_point(['c', 'd', 'e', 'f', 'a'])\
                                                , 4, rotation_point(['c', 'd', 'e', 'f', 'a']) == 4))

print("{0}\n should equal \n{1}\n {2}\n".format(rotation_point([13, 8, 9, 10, 11])\
                                                , 1, rotation_point([13, 8, 9, 10, 11]) == 1))