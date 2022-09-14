
cntr = 0
for i in range(150, 49, -1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i, end=" ")
        cntr += 1
print()

print(f"There are {cntr} prime numbers between 150 and 50")

print("-" * 40)

count = 0

for i in range(50, 150):
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i)
        count += 1
print(f'Total Prime numbers: {count}')
