
def outerFun(fnc):
    def helper():
        print("My info logged into the service")
        fnc()
        print("My info logged out of the service")

    return helper

def normalFun():
    print("I should be called as normal")

print("-" * 40)
outerFun(normalFun)             # no output

print("-" * 40)
outerFun(normalFun)()

print("-" * 40)
normalFun = outerFun(normalFun)
normalFun()

print("-" * 40)
print("-" * 40)

@outerFun
def basicFun():                             # decorator
    print("I should be called as BasicFun")

# basicFun = outerFun(basicFun)
basicFun()



