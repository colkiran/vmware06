
l1 = list(range(1, 11))
print(f"l1 Before :{l1}")
l1.clear()

print(f"l1 After :{l1}")

print("count".center(40, "-"))
l2 = [1, 2, 1, 1, 1, 1, 2, 3, 1, 2, 1,1,1, 1, 2, 3, 1,1, 1, 2,2, 2, 1, 2, 3]
print(f"len(l2) :{len(l2)}")

print(f"1 :{l2.count(1)}")
print(f"2 :{l2.count(2)}")
print(f"3 :{l2.count(3)}")

print("{:*^40}".format("index"))
l1= [1, 2, 3, 1, 2, 1, 1, 1, 1, 1 ,1, 2, 3, 1, 1, 1, 1, 1, 1, 2, 3, 1, 1, 1, 2]
print(f"l1 :{l1}")

print("3 :", l1.index(3))
print("3 :", l1.index(3, l1.index(3) + 1))
print("3 :", l1.index(3, l1.index(3, l1.index(3) + 1) + 1))

print("copy".center(40, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 before  :{l1}")
# copy from l1 to l2
l2 = l1                     # shallow copy -> copies the data along with the address
print("l2 before  :{l2}")

l2.extend([6, 7, 8, 9])
print(f"l2 after  :{l2}")
print(f"l1 after  :{l1}")

print("*" * 40)

l3 = [10, 20, 30, 40, 50]
print(f"l3 before :{l3}")
l4 = l3.copy()                      # deep copy -> only data is shared
print(f"l4 before :{l4}")

l4.insert(1, 15)
l4.insert(3, 25)
l4.insert(5, 35)
print(f"l4 after :{l4}")
print(F"l3 after :{l3}")

print("*" * 40)
l5 = [1, 2, 3, 4, [11, 22, 33, 44, 55], 5]
print(f"l5 before :{l5}")
l6 = l5.copy()
print(f"l6 before :{l6}")

print(f"l6[4] :{l6[4]}")
l6[4].extend([66, 77, 88])
print(f"l6 after :{l6}")
print(f"l5 after :{l5}")

print("*" * 40)
from copy import deepcopy
l7 = [2, 4, 6, 8, 10, [1, 3, 5, 7, 9]]
print(f"l7 before :{l7}")
l8 = deepcopy(l7)
print(f"l8 before :{l8}")

print(l8[5])
l8[5].extend([11, 13, 15])
print(f"l8 after :{l8}")
print(f"l7 after :{l7}")