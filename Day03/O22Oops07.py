
from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def doJob(self):
        pass


class Manager(Employee):

    def doJob(self):
        print("Manager's Job.....")

class Developer(Employee):

    def doJob(self):
        print("Developer's job.....")

def BankJob(emp):
    print("Bankjob started........")
    emp.doJob()
    print("Bankjob completed.........")
    print("-" * 40)


mike = Manager()
david = Developer()

BankJob(mike)
BankJob(david)





