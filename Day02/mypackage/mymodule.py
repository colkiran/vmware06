
guest = "Sachin Tendulkar"

runs = {'test': 18500, 'odi': 24850, 't20': 1200}

sport = ['cricket', 'hockey', 'swimming', 'tennis', 'soccer']

def greet(gname):
    print(f"Greetings Mr.{gname}, Welcome to the event....")

class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")
