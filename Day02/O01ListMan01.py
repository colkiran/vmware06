
l1 = list()
print(f"l1 :{l1}")
print(type(l1))

print("-" * 40)
l2 = [1, 2, 3, 4.6, 5.7, 6.1, 'seven', 'eight', 'nine', 10+1j, 11-3j, True, False]
print(f"l2 :{l2}")
print(type(l2))

print("-" * 40)
l3 = list(range(1, 11))
print(f"l3 :{l3}")
print(type(l3))

print("-" * 40)
l4 = [1, 2, 3, 4.6, 5.7, 6.1, 'seven', 'eight', 'nine', 10+1j, 11-3j, True, False]
print(f"l4 :{l4}")

print("l4[0] :", id(l4[0]))
print("l4[1] :", id(l4[1]))
print("l4[2] :", id(l4[2]))
print("l4[3] :", id(l4[3]))

print("-" * 40)
l5 = list(range(1, 11))
print(f"l5 :{l5}")

# read
print(f"l5[3] :{l5[3]}")
print(f"l5[8] :{l5[8]}")

# iterate list
for i in l5:
    print(i, end=" ")
print()

for i in range(0, len(l5)):
    print(l5[i],end=" ")
print()

# modify
print(f"l5 :{l5}")
l5[4] = 5.5
l5[6] =7.9
print(f"l5 :{l5}")

# cannot add new elements into the list

# delete
del l5[6]
del l5[4]
print(f"l5 :{l5}")

print("-" * 40)

values = list(range(10, 40, 10))
print(f"values :{values}")
a, b, c = values                        # unpack the list
print(a, b, c, sep=", ")

print("-" * 40)
values = list(range(10, 101, 10))
print(f"values :{values}")

a, b, *c = values                   # c can store more than one value in the form of a list
print(a, b, c)

a, *b, c = values
print(a, b, c)

*a, b, c = values
print(a, b, c)

print("-" * 40)
lst1 = [1, 2, 3, 4, 5]
lst2 = [11, 22, 33, 44, 55]

print(f"lst1 :{lst1}")
print(f"lst2 :{lst2}")

lst3 = [lst1, lst2]
print(len(lst3))
print(f"lst3 :{lst3}")

print("-" * 40)
lst4 = [*lst1, *lst2]
print(len(lst4))
print(f"lst4 :{lst4}")

print("-" * 40)
lst1 = [1, 2, 3, 4, 5]
print(f"lst1 :{lst1}")
res = lst1 * 2
print(f"res :{res}")



