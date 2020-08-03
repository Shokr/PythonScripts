# Instance attributes are accessed by: object.attribute
# Attributes are looked First in the instance and THEN in the class
import random


class Vehicle:
    # Class Methods/ Attributes
    def type(self):
        # NOTE: This is not a class attribute as the variable is binded to self. Hence it becomes
        # instance attribute
        # Setting the instance attribute
        self.randomValue = random.randint(1, 10)


car = Vehicle()
car.type()  # Calling the class Method
print(car.randomValue)  # Calling the instance attribute

######################################################################################################
# This program shows the order in which the classes are accessed in case of multiple inheritance
# Python uses DEPTH FIRST SEARCH algorithm for lookups


class A(object):
    @staticmethod
    def doThis():
        print("Doing this in A")


class B(A):
    pass


# If class C was also eing derived from A then the lookup order would be D,B,C,A
class C(object):
    @staticmethod
    def doThis():
        print("Doing this in C")


class D(B, A):
    pass


if __name__ == "__main__":
    dObj = D()
    dObj.doThis()  # A method gets called because order for lookup is D,B,A,C this is shown by function mro

    print(D.mro())

######################################################################################################

# In this example we will see how the private variables work in Python


class Person(object):
    def __init__(self, name):
        self.name = name
        self.__education = "Engineer"  # Private Variable

    def displayInfo(self):
        name = self.name
        education = self.__education  # Can only be accessed within the class
        print("My name is", name, "and I have completed my", education)


if __name__ == "__main__":
    myObj = Person("Shokr")
    myObj.displayInfo()
    print(myObj.name)  # Can be accessed as it is public variable
    # print(myObj.__education)                  # Throws an error
    # Private variable can be accessed like this but NEVER EVER
    print(myObj._Person__education)
    # do this please!!

######################################################################################################

# In this example we will see what are Python Magic Methods (or Special Methods) and how to overload them
# Now why these methods are called Magic or Special methods anyway? The reason is that these
# methods are invoked directly after creation of a class instance. For example:
# __init__ is a Magic method. Also __str__, __repr__, __add__ are all magic methods.


class Employee(object):
    def __init__(self, firstname, lastname, salary=0):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary

    def __str__(self):
        return "Full Name: " + self.firstname + " " + self.lastname

    # Implements behaviour for built in type comparison to int
    def __int__(self):
        return self.salary

    # For overloading the (==)
    def __eq__(self, other):
        return self.salary == other.salary

        # For overloading the (+)

    def __add__(self, other):
        return self.salary + other.salary

    # For overloading the (*)
    def __mul__(self, other):
        return self.salary * other.salary


if __name__ == "__main__":
    Omkar = Employee("Omkar", "Pathak", 1000)
    Jagdish = Employee("Jagdish", "Pathak", 2000)
    # Full Name: Omkar Pathak (This output because of __str__ method overloading)
    print(Omkar)
    print(Jagdish)  # Full Name: Jagdish Pathak
    # 3000 (This output because of __add__ method overloading)
    print(Omkar + Jagdish)
    print(Omkar * Jagdish)  # 2000000 (__mul__)
    print(int(Omkar))  # 1000 (__int__)
    print(int(Jagdish))  # 2000 (__int__)
    print(Omkar == Jagdish)

######################################################################################################

# A Python generator is a function which returns a generator iterator (just an object we can iterate over)
# by calling yield


def simpleGenerator(numbers):
    i = 0
    while True:
        check = input("Wanna generate a number? (If yes, press y else n): ")
        if check in ("Y", "y") and len(numbers) > i:
            yield numbers[i]
            i += 1
        else:
            print("Bye!")
            break


for number in simpleGenerator([10, 11, 12, 14]):
    print(number)
