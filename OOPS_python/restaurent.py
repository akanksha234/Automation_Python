from datetime import datetime


#############################Menu Class###############################
class Menu():

    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        start_time = "".join(start_time.split())
        end_time = "".join(end_time.split())
        self.start_time = datetime.strptime(start_time, '%I%p').time().strftime('%I%p')
        self.end_time = datetime.strptime(end_time, '%I%p').time().strftime('%I%p')

    def __repr__(self):
        return self.name + " menu avaialble from {} to {}".format(self.start_time, self.end_time)

    def calculate_bill(self, purchased_items):
        total_bill = 0
        for item in purchased_items:
            total_bill += self.items[item.lower()]
        return total_bill

######################################Franchise clas##################################################
class Franchise():

    def __init__(self, address, *menus):
        self.address = address
        self.menus = menus

    def __repr__(self):
        return "Franchise address: " + self.address

    def available_items(self, time_):
        today11am = datetime.now().replace(hour=11)
        today5pm = datetime.now().replace(hour=17)
        today11pm =datetime.now().replace(hour=23)
        today4pm =datetime.now().replace(hour=16)
        today3pm = datetime.now().replace(hour=13)
        today6pm =datetime.now().replace(hour=18)
        today9pm = datetime.now().replace(hour=21)
        if(time_ >= today11am and time_ < today3pm):
            return "brunch and kids"
        if(time_ >= today3pm and time_ <= today4pm):
            return "brunch, early_bird and kids"
        if(time_ > today4pm and time_ < today5pm):
            return "early_bird and kids"
        if (time_ >= today5pm and time_ <= today6pm):
            return "early_bird, dinner and kids"
        if(time_ >= today6pm and time_ <= today9pm):
            return "dinner and kids"
        if(time_ > today9pm and time_ <= today11pm):
            return "dinner"
        return "Sorry!! No menu available at this time."

###############################Business Class##########################################

class Business():

    def __init__(self, name, *franchises):
        self.name = name
        self.franchises = franchises


    def __repr__(self):
        return "Hi! welcome to {name_of_business}." \
               "\nWe have {number_of_franchises} franchises available : \n{franchises}"\
                .format(name_of_business= self.name, franchises= self.franchises, number_of_franchises=len(self.franchises))

########################main code######################

#all items and menus created
#brunch_items
brunch_items = {
    'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00,
    'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50,
}
brunch = Menu('brunch', brunch_items, '11am', '4pm')
#early_items
early_items = {
    'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00,
    'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50,
    'espresso': 3.00,
}
early_bird = Menu('early_bird', early_items, '3pm', '6pm')
#dinner
dinner_items = {
    'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00,
    'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
dinner = Menu('dinner', dinner_items, '5 pm', '11pm')
#kids
kids_items = {
    'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
kids = Menu('kids', kids_items, '11am', '9pm')


####################purchase and orders########################
purchased_items = ['PAncakes', 'home fries', 'coffee']

total_bill = brunch.calculate_bill(purchased_items=purchased_items)
print("Hi!!!\nyour brunch bill is: ", str(total_bill) + "$")

purchased = ['SALUMERIA plate', 'MUSHROOM RAVIOLi (vegan)']
bill = early_bird.calculate_bill(purchased)
print("Hi!!\nYour early bird bill is: {}$".format(bill))

print(brunch)
print(early_bird)
print(dinner)
print(kids)

flagship_store = Franchise("1232 West End Road", early_bird, brunch, dinner, kids)
new_installment = Franchise("12 East Mulberry Street", early_bird, brunch, dinner, kids)
print( new_installment.available_items(datetime.now().replace()) )
#our first business
name_of_business = "Basta Fazoolin' with my Heart"
business = Business(name_of_business, flagship_store, new_installment )
print(business)

######using classes example###########
arepa_items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
arepa_menu = Menu(name='arepe', items=arepa_items, start_time='10am', end_time='8pm' )
arepas_place = Franchise( "189 Fitzgerald Avenue", arepa_menu)
arepa_business = Business("Take a' Arepa", arepas_place )
print(arepa_business)
