
def greet():
    print("Greetings Mr. Sachin, Welcome to the event....")

def greetGst(gname):
    print(f"Greetings Mr. {gname}, Welcome to the event.....")

# city is called as default arg and gname is called as non default arg
def greetGstCty(gname, city="Mumbai"):
    print(f"Greeting Mr.{gname} from {city}, Welcome to the event.......")


greet()
greetGst("Rahul")
print("-" * 40)
greetGstCty("Sachin")
greetGstCty("Rohit")
greetGstCty("Rahul", "Bangalore")

print("-" * 40)
def admsn(name, dob, gender, qlf, contno, adr, city):
    # *args - like a list
    # **kwargs - like a dictionary
    print(f"Name            :{name}")
    print(f"DOB             :{dob}")
    print(f"Gender          :{gender}")
    print(f"Qualification   :{qlf}")
    print(f"Contact No.     :{contno}")
    print(f"Address         :{adr}")
    print(f"City            :{city}")

admsn("Jack", "19/04/1987", "Male", "BE", "29299229", "Indira Nagar, Mumbai", "Mumbai")
print("-" * 40)
admsn(gender="Female", qlf="MBA", city="Hyderabad", dob="04/10/1989", contno="22992565",
      name="Jill", adr="madhapur, hyderabad")

# Variable length args
print("-" * 40)
def productAll(*numbers):
    print(numbers)
    prod = 1
    for number in numbers:
        prod *= number
    return prod

print(f"Multiply all :{productAll(1, 2, 3, 4, 5)}")

print("-" * 40)
def extractDetails(**details):
    print(details)
    for k, v in details.items():
        print(k, "=>", v)

extractDetails(name="Rahul", runs=105, oppn='srilanka', venue="China Sawmy")

print("-" * 40)
# function return values
def multiplyMe(x, y):
    return x * y

print("%i * %i = %i" % (10, 20, multiplyMe(10, 20)))

print("-" * 40)

def basicArithematic(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    quot = x / y
    return sum, diff, prod, quot

res = basicArithematic(20, 8)
print(f"res :{res}")

# python supports recursive calls
# find the factorial of a number
# find the fibanocci series
print("-" * 40)
def fact(n):
    if n < 2:
        return n
    return n*fact(n-1)
print(fact(5))

def fib(x):
    if x == 0: return 0
    if x == 1: return 1
    return fib(x - 1) + fib(x - 2)

nterms = 8
    # int(input("enter the number of iterations :"))
print("fibanocci series")
for i in range(nterms):
    print(fib(i), end=" ")
print()

print("-" * 40)
# doc string

def fun():
    # this is a comment
    "This is a doc string"
    print("hello world")

fun()
print(fun.__doc__)

print("-" * 40)

def fun1(x, y):
    """
    fun1(x, y)

    function fun1 takes two arguments and returns
        a. if x and y are integers then we get the sum of x and y as result
        b. if x and y are strings then we get the concatenated string as result
        c. if they are not the same data type then will throw and error

    """

    return x + y

print(fun1(10, 20))
print(fun1("hello ", "world"))

print("-" * 40)
help(fun1)
