
glbx = 100

def fun(a):             # local variable
    global glbx         # don't assign any value in this line
    glbx = 250
    print(f"Inside :{glbx}")
    print(f"a :{a}")
    b = 50
    print(f"b :{b}")            # local variable


print(f"before :{glbx}")

fun(15)

print(f"after :{glbx}")
