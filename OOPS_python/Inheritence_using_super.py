from sortedcontainers import sortedlist



class SortedList(list):

    def __init__(self, sample_list):
        super().__init__(sample_list)
        super().sort()

    def append(self, value):
        super().append(value)
        super().sort()

    def __repr__(self):
        return str(sorted(self))




obj = SortedList([3, 4, 1, 8, 2, 3, 23, 78, 12])
print(obj)
obj.extend([7, 8])
print(obj)