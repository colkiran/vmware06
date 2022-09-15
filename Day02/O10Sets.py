
s1 = set()
print(f"s1 :{s1}")
print(type(s1))

print("-" * 40)
s2 = {1, 2, 3, 4, 5.1, 6.3, 7.2, 'eight', 'nine', 'ten', 11 + 0j, 12- 2j, True, False}
print(f"s2 :{s2}")
print(type(s2))

print("-" * 40)
s3 = set(range(1, 11))
print(f"s3 :{s3}")
print(type(s3))

print("-" * 40)
s4 = {1, 2, 3, 4}
print(f"s4 :{s4}")
print(type(s4))

# add values into the set
print("-" * 40)
s4.add(1)
s4.add(5)
s4.add(3)
s4.add(6)
s4.add(2)
s4.add(7)

print(f"s4 :{s4}")

print("-" * 40)
s4.update([1, 5, 7])
s4.update([7, 8, 9])
s4.update([3, 6, 9])
s4.update([10, 2, 4])

print(f"s4 :{s4}")

# delete values
res = s4.pop()
print(f"res :{res}")

res = s4.pop()
print(f"res :{res}")

print(f"s4 :{s4}")

s4.remove(10)
s4.remove(5)
print(f"s4 :{s4}")

s4.discard(4)
s4.discard(7)
s4.discard(10)
print(f"s4 :{s4}")

print("-" * 40)
A = {1, 2, 3, 4, 5, 6}
B = {5, 6, 7, 8, 9, 10}

print(f"A :{A}")
print(f"B :{B}")

print(f"A union B :{A | B}")
print(f"B union A :{B.union(A)}")

print(f"A intersection B :{A & B}")
print(f"B intersection A :{B.intersection(A)}")

print(f"A difference B :{A - B}")
print(f"B difference A :{B.difference(A)}")

print(f"A symmetric difference B :{A ^ B}")
print(f"B symmetric difference A :{B.symmetric_difference(A)}")

print("-" * 40)
# frozen set = immutable
a = frozenset({1, 2, 3, 4, 5})
print(f"a :{a}")
print(type(a))
