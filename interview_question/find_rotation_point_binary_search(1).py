# find rotation point
# O(logN) time requirement
# return index of "rotation point" element

def rotation_point(rotated_list):
    low = 0
    high = len(rotated_list)
    mid = int((low+high)/2)
    shortest = 0
    shortest_element_position = 0

    while True:
        next = mid + 1
        previous = mid - 1
        if(rotated_list[mid] < rotated_list[next]):
          if(rotated_list[mid] < rotated_list[previous]):
              shortest_element_position = mid
              shortest  = rotated_list[mid]
              break
          else:
              mid = previous
        else:
          mid = next

    if(mid < 0):
        return len(rotated_list) + mid

    return mid






#### TESTS SHOULD ALL BE TRUE ####
print("{0}\n should equal \n{1}\n {2}\n".format(rotation_point(['a', 'b', 'c', 'd', 'e', 'f']), 0, rotation_point(['a', 'b', 'c', 'd', 'e', 'f']) == 0))

print("{0}\n should equal \n{1}\n {2}\n".format(rotation_point(['c', 'd', 'e', 'f', 'a']), 4, rotation_point(['c', 'd', 'e', 'f', 'a']) == 4))

print("{0}\n should equal \n{1}\n {2}\n".format(rotation_point([13, 8, 9, 10, 11]), 1, rotation_point([13, 8, 9, 10, 11]) == 1))