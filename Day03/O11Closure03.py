
def outerFun(greet):
    def innerFun(gname):
        print(greet, gname)
    return innerFun

engGrt = outerFun("Welcome")
hndGrt = outerFun("Namaskar")
tmlGrt = outerFun("Vanakam")

# simple curry
engGrt("Sachin")
hndGrt("Jadeja")
tmlGrt("Dhoni")
