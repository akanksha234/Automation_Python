class Circle:
    pi = 3.14

    #__init__ can only return None but no other value
    def __init__(self, diameter):
        self.radius = diameter/2
        self.diameter = diameter

    #__repr__ takes no argument other than self
    #__repr__ must only return string
    def __repr__(self):
        return "circle of diameter {} inches".format(self.diameter)

    def area(self):
        return self.pi * (self.radius ** 2)


pizza_area = Circle(12).area()
teaching_table_area = Circle(36).area()
round_room_area = Circle(11460).area()

print("pizza area ---> {}\nteaching table --->{}\nround room area --->{}".format(pizza_area, teaching_table_area, round_room_area))
print(Circle(12))