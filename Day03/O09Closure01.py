
def outerFun(gname):             # nested function
    guest = f"Mr.{gname}"

    def innerFun():

        print("Hello World")
        print(guest)

    innerFun()

outerFun("Rahul")