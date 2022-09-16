

def outerFun(fnc):

    def innerFun(a, b):
        if b > a:
            a, b = b, a             # swap values
        print(fnc(a, b))

    return innerFun

@outerFun
def diff(x, y):
    return x - y

diff(10, 20)
diff(50, 30)
diff(30, 50)