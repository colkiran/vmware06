
letters = ['a', 'b', 'c', 'd', 'e']
print(f"letters :{letters}")

print("-" * 40)
for letter in letters:
    print(letter, end=" ")
print()

print("-" * 40)
for letter in enumerate(letters):
    print(letter, end=" ")
print()

print("-" * 40)
for letter in enumerate(letters):
    print(letter[0],"\t", letter[1])

print("-" * 40)
for index, letter in enumerate(letters):
    print(index, "\t", letter)

print("-" * 40)
mylist = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"mylist :{mylist}")

print("-" * 40)
for lst in mylist:
    print(lst)

print("-" * 40)
for ind, lst in enumerate(mylist):
    print(ind, '\t', lst)

print("-" * 40)
for ind, lst in enumerate(mylist):
    print(f"List({ind})")
    for idx, num in enumerate(lst):
        print(f"\t{idx}\t{num}")

# print("-" * 40)
# print(dir(lst))

# append, extend, insert

print("{:-^40}".format("append"))
l1 = list(range(1, 6))
print(f"l1 :{l1}")

l1.append(6)
l1.append(7)
l1.append(8)
print(f"l1 :{l1}")

l1.append([9, 10, 11, 12, 13])
print(f"l1 :{l1}")

print(f"l1[8] :{l1[8]}")
print(f"l1[8][1:4] :{l1[8][1:4]}")

print("extend".center(40, "-"))
l2 = list(range(2, 10, 2))
print(f"l2 :{l2}")

l2.extend([10, 12, 14])
l2.extend([16, 18, 20])
print(f'l2 :{l2}')

print("insert".center(40, "-"))
l1 = list(range(1, 6))
print(f"l1 :{l1}")

l1.insert(1, 1.5)
l1.insert(3, 2.5)
l1.insert(5, 3.5)
l1.insert(7, 4.5)

print(f"l1 :{l1}")
l2 = [1, 2, 3]
l2.insert(10, 5)
print(f"l2 :{l2}")

# pop, remove
print("pop".center(40, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")

res = l1.pop(2)
print(f"res :{res}")

res = l1.pop(3)
print(f"res :{res}")
print(f"l1 :{l1}")

res = l1.pop()
print(f"res :{res}")
print(f"l1 :{l1}")

print("remove".center(40, "-"))
l1  = [1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 2, 2, 1, 2, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 3]
print(f"l1 :{l1}")
l1.remove(2)

print(f"l1 :{l1}")

while l1.count(1):
    l1.remove(1)

print(f"l1 :{l1}")




# while True:
#     try:
#         l1.remove(1)
#     except ValueError:
#         break
#
# print(f"l1 :{l1}")
