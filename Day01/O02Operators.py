
print("a :", ord("a"))
print("z :", ord("z"))
print("A :", ord("A"))
print("Z :", ord("Z"))

print("bitwise operator".center(40, "-"))
print(f"5 | 3 => {5 | 3}")
print(f"5 & 3 => {5 & 3}")
print(f"5 ^ 3 => {5 ^ 3}")
print(f"5 << 1 :{5 << 1}")
print(f"8 << 1 :{8 << 1}")
print(f"5 << 2 :{5 << 2}")
print(f"16 >> 1 :{16 >> 1}")
print(f"5 >> 1 :{5 >> 1}")

print(~0)
print(~5)

print("ternary".center(40, "-"))
age = 10
print("Eligible" if age >= 18 else "not eligible")
