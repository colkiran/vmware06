
def outerFun(greet):
    def innerFun(sep):
        def innerMostFun(gname):
            import emojis
            emojized = emojis.encode(greet + " :" + sep + ": " + gname)
            print(emojized)
        return innerMostFun
    return innerFun


kndGrt = outerFun("Namaskara")

kndTgr = kndGrt("tiger")

kndTgr("Prabhakar")

"""
engGrt = outerFun("Welcome")
hndGrt = outerFun("Namaskar")

engSln = engGrt("----->")
engDln = engGrt("=====>>")

engSln("Sachin")
engDln("Rahul")
"""