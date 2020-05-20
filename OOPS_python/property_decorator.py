class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        # self.email = first + '.' + last + '@gmail.com'

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, new_name):
        self.first, self.last = new_name.split(' ')

    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None


emp_1 = Employee('John', 'Smith')
emp_1.first = 'Jim'
#now if we suddenly change the first nale,
# the email attribute is not automatically updated unless
#we update it manually
#if we decide to set a mthod then it will break the code for everyone else who was using that class
#and email attribute, this is where property decorator comes handy,
#if we use property decorator abogve some method it will act as an attribute
emp_1.fullname = 'Akanksha Singh'
print(emp_1.first)
print(emp_1.last)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.first
print(emp_1.first)

