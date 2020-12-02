# class methods in python
class Employee:

    increment = 1.5
    no_of_employees = 0

    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        # self.increment = 1.4
        Employee.no_of_employees += 1               # access class variable using classname.classvariable

    # let say we want to run a function whose relation is only with class variables not instance variables
    # in this example "increment" is class variable and if we want to change increment
    # we will not pass self in argument(we don't need object, we have to handle class variable only), so we will
    # make class method
    # The @classmethod decorator, is a builtin function decorator
    # class method in python - a special type of method which takes class name as an argument
    @classmethod
    def change_increment(cls, incrementamount):
        cls.increment = incrementamount

    def increase(self):
        self.salary = int(self.salary * Employee.increment)

    # Class methods as Alternative constructor
    @classmethod
    def from_str(cls, emp_string):
        fname, lname, salary = emp_string.split("-")    # parsing we are doing here
        return cls(fname, lname, salary)

    # if we don't want to deal with instance as well as class variable, in that case what we will do
    # in that case we would be wanted that our function neither take class nor self as an argument
    # use decorator @staticmethod
    # In general, static methods know nothing about class state. They are utility type methods that take some parameters
    # and work upon those parameters. On the other hand class methods must have class as parameter.
    # We generally use static methods to create utility functions.
    @staticmethod
    def isopen(day):
        if day == 'sunday':
            return "false"
        else:
            return "true"

Mayur = Employee("Mayur", "Mochi", 100000)
Raj = Employee.from_str("Raj-Mochi-100000")

print(Mayur.salary)
Mayur.change_increment(2)       # we wanted to change Employee class one variable only that's why we made a method
Mayur.increase()                # which takes class as an argument not an object (we didn't want to pass whole object)
print(Mayur.salary)

# There are following methods to print multiple variables,
# Method 1: Passing multiple variables as arguments separating them by commas
print("First name : ", Raj.fname, "Last name : ", Raj.lname , "salary : ", Raj.salary, sep='\n')
# Method 2: Using format() method with curly braces ({})
# output ---> Raj, Mochi, 100000
print("{}, {}, {}".format(Raj.fname, Raj.lname, Raj.salary))
# output ---> first name: Raj, last name :Mochi, salary:100000
print("first name: {}, last name :{}, salary:{}".format(Raj.fname, Raj.lname, Raj.salary))
# Method 3: Using format() method with numbers in curly braces ({0})
# output --> Raj, Mochi, 100000
print("{0}, {1}, {2}".format(Raj.fname, Raj.lname, Raj.salary))
# output ---> first name: Raj, last name: Mochi, salary: 100000
print("first name: {0}, last name: {1}, salary: {2}".format(Raj.fname, Raj.lname, Raj.salary))
# Printing all values 2-2 times
print("{0} {0} {1} {1} {2} {2}".format(Raj.fname, Raj.lname, Raj.salary))

# Running with the help of class
print(Employee.isopen("monday"))

# Running with the help of instance
# Raja = Employee("Raja", "Mochi", 100000)
Raja = Employee.from_str("Raja-Mochi-100000")
print(Raja.isopen("sunday"))