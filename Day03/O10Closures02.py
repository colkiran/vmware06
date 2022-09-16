
def outerFun(gname):             # HOF - Higher order function
    guest = f"Mr.{gname}"

    def innerFun():

        print("Hello World")
        print(guest)

    return innerFun

outerFun("Sachin")()                # calls innerfun

print("-" * 40)
infun = outerFun("Rahul")

print("hello world")
print("hello world")
print("hello world")

print("-" * 40)
infun()

print("-" * 40)
print(outerFun.__name__)
print(outerFun("sachin").__name__)

