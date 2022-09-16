
class Animal:
    def __init__(self):
        print("Animal Ctor.....")
        self.a = 10

    def eat(self):
        print("animals eat......")

class Bird(Animal):

    def __init__(self):                     #overload parent class constructor
        super().__init__()
        print("Bird Ctor.....")
        self.b = 20

    def fly(self):
        print("birds fly.......")

class Fish(Animal):

    def __init__(self):
        super().__init__()
        print("Fish Ctor.....")
        self.f = 30

    def swim(self):
        print("fishes swim......")

cuckoo = Bird()
cuckoo.eat()
cuckoo.fly()

dolphin = Fish()
dolphin.eat()
dolphin.swim()

print("-" * 40)
print(cuckoo.__dict__)

print("-" * 40)
print(dolphin.__dict__)


