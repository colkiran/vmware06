
class Animal:

    def eat(self):
        print("Animals eat.......")

class Bird(Animal):

    def fly(self):
        print("birds fly.....")

class Chicken(Bird):

    def disp(self):
        print("Chicken's are breeded for consmption.....")

    def fly(self):
        print("Chicken's seldom fly.......")


chic = Chicken()
chic.eat()
chic.fly()
chic.disp()


