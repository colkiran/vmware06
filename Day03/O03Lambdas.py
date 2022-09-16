
def add(x, y):
    return x + y

a = add

print(a(10, 20))

print("-" * 40)

b = lambda x, y: x + y
res = b(100, 200)
print(f"res :{res}")

# map, filter and reduce (functools)

# map - implement the expression on all the number in a list
l = list(range(1, 11))
print(f"l :{l}")

squares = list(map(lambda x: x ** 2, l))
print(f"squares :{squares}")

print("-" * 40)
months = ['dec', 'aug', 'apr', 'jul', 'jun', 'oct', 'mar', 'nov', 'jan', 'may', 'feb', 'sep']
# sort these months
from calendar import month_name
print(f"month_name :{list(month_name)}")
print("-" * 40)
print(f"months :{months}")

res = sorted(months, key=list(map(lambda x: x.lower()[0:3], list(month_name))).index, reverse=True)
print(f"res :{res}")

print("filters".center(40, "-"))
l = list(range(1, 25))
print(f"l :{l}")

print("-" * 40)
res = list(filter(lambda x: x % 3 == 0, l))
print(f"res :{res}")

print("-" * 40)
res = list(filter(lambda x: x % 2 == 0, l))
print(f"res :{res}")

print("-" * 40)
res = list(filter(lambda x: x % 5 == 0, l))
print(f"res :{res}")

print("-" * 40)
sentence = "the quick brown fox jumps over the lazy dog"
print(f"sentence :{sentence}")
res = list(filter(lambda x: x != "the", sentence.split()))
print(f"res :{res}")

print("reduce".center(40, "-"))
from functools import reduce
l = [1, 5, 8, 10, 15, 12, 9, 1, 3, 11, 7, 14]
print(f"l :{l}")

res = reduce(lambda x, y: x if x > y else y, l)
print(f"res :{res}")

print("-" * 40)
res = reduce(lambda x, y: x + y, l)
print(f"res :{res}")

# if we use lambda syntax to iterate a collection (list, dictionary) we call it as comprehensions
