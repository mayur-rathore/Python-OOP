# The pass statement is used as a placeholder for future code.
# When the pass statement is executed, nothing happens, but you avoid getting an error when empty code is not allowed.
# Empty code is not allowed in loops, function definitions, class definitions, or in if statements

# having an empty for loop like this, would raise an error without the pass statement
for x in [0, 1, 2]:
    pass

# About class variables and instance variables


class Employee:

    increment = 1.5
    no_of_employees = 0

    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        # self.increment = 1.4
        Employee.no_of_employees += 1               # access class variable using classname.classvariable

    def increase(self):
        # self.increment first search in instance variable (i.e. inside __init__ constructor) , if it is not available
        # there then it will check in class variable (i.e. increment = 1.5)
        # self.salary = int(self.salary * self.increment)
        self.salary = self.salary * Employee.increment


print(Employee.no_of_employees)                     # print 0 because no employee creates yet
Mayur = Employee("Mayur", "Mochi", 100000)          # fname, lname, salary are personal variables of instance i.e.Mayur,
print(Employee.no_of_employees)                     # print 1 because one employee "Mayur" created
Raj = Employee("Raj", "Mochi", 100000)              # Raj object while increment is class's personal variable
print(Employee.no_of_employees)                     # print 2 because two employees "Mayur" and "Raj" created


print(Mayur.salary)
Mayur.increase()
print(Mayur.salary)

print(Mayur.__dict__)           # it will list out all the instances of variable (instances of Mayur can be seen in
Mayur.increment = 9             # constructor) output = {'fname': 'Mayur', 'lname': 'Mochi', 'salary': 150000.0}
print(Mayur.__dict__)           # output = {'fname': 'Mayur', 'lname': 'Mochi', 'salary': 150000.0, 'increment': 9}

print(Employee.__dict__)        # list out all the instances/variables of class

