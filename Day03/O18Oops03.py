
class Animal:
    def __init__(self):
        print("Animal Ctor.....")
        self.a = 10

    def eat(self):
        print("animals eat......")

class Bird(Animal):

    def fly(self):
        print("birds fly.......")

class Fish(Animal):

    def swim(self):
        print("fishes swim......")


cuckoo = Bird()
cuckoo.fly()
cuckoo.eat()

dolphin = Fish()
dolphin.swim()
dolphin.eat()

print("-" * 40)
print(cuckoo.__dict__)

print("-" * 40)
print(dolphin.__dict__)