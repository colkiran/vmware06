
"""
object is the base class of all classes
"""

class Player:                   # pascal casing

    def get_runs(self):
        print("Runs scored.....")

sachin = Player()                   # calls the default constructor
sachin.get_runs()

print("-" * 40)
print(type(sachin))
print(isinstance(sachin, Player))
print(isinstance(sachin, object))
print(isinstance(sachin, str))
