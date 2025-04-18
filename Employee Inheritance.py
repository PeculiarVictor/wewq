class Person( object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
class Employee(Person):
    def __init__(self, name, id number,salary, post):
        self.salary = salary
        self.post = post


        Person.__init__(self, name, id number)
a = Employee("Rahul", 886012, 200000, "Intern")
a.display()
