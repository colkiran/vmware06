
"""
self will have the name of the object that called the method

"""
class Player:                   # pascal casing

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_detail(self):
        print(f"Name is {self.name}\nAge is {self.age}")

ply1 = Player("Sachin", 36)
ply1.get_detail()

print("-" * 40)

ply2 = Player("Rahul", 34)
ply2.get_detail()

print("-" * 40)
print(ply1.__dict__)

print("-" * 40)
print(ply2.__dict__)
