
def outerFun(fnc):                  # HOF
    loginfo = "Logging into the service..."

    def innerFun(*args):
        print(loginfo)
        fnc(*args)
        print("-" * 40)

    return innerFun

def fun():
    print("fun does not take an arg")

def fun1(x):
    print(f"fun1 takes one arg :{x}")

def fun2(x, y):
    print(f"fun2 takes two arg :{x} {y}")

def fun3(x, y, z):
    print(f"fun3 takes three arg :{x} {y} {z}")

infun = outerFun(fun)
infun()
print("-" * 40)

infun = outerFun(fun1)
infun(10)
print("-" * 40)

infun = outerFun(fun2)
infun(10, 20)
print("-" * 40)

infun = outerFun(fun3)
infun(10, 20, 30)
print("-" * 40)
