
def outerFun(gname):
    chiefGuest = f"Mr. {gname}"

    def innerFun():
        nonlocal chiefGuest
        print("hello world")
        chiefGuest = f"Mr. Rahul"
        print(chiefGuest)

    innerFun()
    print(f"cheifGuest :{chiefGuest}")


outerFun("Sachin")
