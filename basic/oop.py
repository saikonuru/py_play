import os

os.system("cls")


class Person:
    def __init__(self, name, age):  # constructor dunder methods
        self.name = name
        self.age = age

    # def SetValue(self, name, age):
    #     self.name = name
    #     self.age = age

    def GetValue(self):
        print("Name : {}, Age: {}".format(self.name, self.age))


# p = Person()
name = input("Enter Name: ")
age = input("Enter Age: ")
# p.SetValue(name, age)
p = Person(name, age)

p.GetValue()
