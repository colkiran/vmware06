
class Animal:

    def __init__(self):
        print("Animal Ctor.....")
        self.a = 10

    def eat(self):
        print("animals eat......")

    def fun(self):
        print("fun method of animal class")

class Person:

    def __init__(self):
        print("Person Ctor.....")
        self.p = 20

    def talk(self):
        print("Person talks......")

    def fun(self):
        print("fun method of person class")


class Girl(Animal, Person):

    def __init__(self):
        super().__init__()
        Person.__init__(self)
        print("Girl Ctor.......")
        self.g = 30



grace = Girl()
grace.eat()
grace.talk()
grace.fun()

print(grace.__dict__)