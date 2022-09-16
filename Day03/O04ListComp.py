
l1 = [x ** 2 for x in range(1, 11)]
print(f"l1 :{l1}")

print("-" * 40)
sentence = "the quick brown fox jumps over the lazy dog"
print(f"sentence :{sentence}")

print("-" * 40)
words = [(word, len(word)) for word in sentence.split()]
print(f"words :{words}")

print("-" * 40)
words = [(word, len(word)) for word in sentence.split() if word != "the"]
print(f"words :{words}")
print("-" * 40)
fruits = [
    ('apple', 285),
    ('orange', 140),
    ('grapes', 115),
    ('banana', 65),
    ('Pineapple', 80),
    ('strawberry', 350),
    ('gauva', 90),
    ('water melon', 70)
]

prices = ["fruit" for fruit in fruits]
print(f"prices :{prices}")

print("-" * 40)
prices = [fruit for fruit in fruits]
print(f"prices :{prices}")

print("-" * 40)
prices = [fruit[0] for fruit in fruits]
print(f"prices :{prices}")

print("-" * 40)
prices = [fruit[1] for fruit in fruits]
print(f"prices :{prices}")

print("-" * 40)
prices= [fruit[1] * 0.9 for fruit in fruits]
print(f"prices :{prices}")

print("-" * 40)
prices= [fruit[1] * 0.75 for fruit in fruits]
print(f"prices :{prices}")

print("-" * 40)
prices = [(fruit[0], fruit[1], fruit[1] * 0.9, fruit[1] * 0.75) for fruit in fruits]
print(f"prices :{prices}")

print("-" * 40)
prices = [(fruit[0], fruit[1], fruit[1] * 0.9, fruit[1] * 0.75) for fruit in fruits if fruit[1] > 100]
print(f"prices :{prices}")

print("-" * 40)
lst1 = [1, 2, 3, 4]
lst2 = [11, 22, 33, 44, 55]

print(f"lst1 :{lst1}")
print(f"lst2 :{lst2}")

print(list(zip(lst1, lst2)))
print(list(zip("ABCD", lst1, lst2)))

print("-" * 40)
combine = [(f, s) for f in lst1 for s in lst2]
print(combine)
