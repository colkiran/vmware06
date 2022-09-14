
# conversions
print("Conversions".format(40, "-"))
print("{val} {val} {val}".format(val="A"))
print("{val!s} {val!r} {val!a}".format(val="A"))

print("The number {num} {num} {num}".format(num=36))
print("The number {num} {num:f} {num:b}".format(num=36))
print("The number {num:10} {num:f} {num:b}".format(num=36))
print("The number {num:5} {num:f} {num:b}".format(num=36))
print("The number {num:5} {num:f} {num:b}".format(num=3654698751))
print("The number {num:5} {num:f} {num:b}".format(num=36))

print("Alignment".center(40, "-"))
print("{num:15}Sachin".format(num=3))
print("{num:15}Sachin".format(num="Ramesh"))
print("{}".format("Sachin Tendulkar"))
print("{:.6}".format("Sachin Tendulkar"))

print("-" * 40)
from math import pi
print("{pi:10.2}".format(pi=pi))
print("{pi:10.3}".format(pi=pi))
print("{pi:10.4}".format(pi=pi))
print("{pi:10.5}".format(pi=pi))

print("Alignment".center(40, "-"))
print("{:15.2f}".format(pi))
print("{:<15.2f}".format(pi))                # left align
print("{:^15.2f}".format(pi))                # center align
print("{:>15.2f}".format(pi))                # right align
print("{:<015.2f}".format(pi))                # left align
print("{:^015.2f}".format(pi))                # center align
print("{:>015.2f}".format(pi))                # right align

print("-" * 40)
print("{:^40}".format("Python"))
print("{:-^40}".format("Python"))
print("{:-<40}".format("Python"))
print("{:->40}".format("Python"))


print("{:-^40}".format("Python"))
print("Python".center(40, "-"))

print("-" * 40)
print("\n")
width = 50
price_width = 10
item_width = width - price_width

header_fmt = "{{:{}}}{{:>{}}}".format(item_width, price_width)
fmt = "{{:{}}}{{:>{}.2f}}".format(item_width, price_width)
print("-" * width)
print(header_fmt.format("Item", "Price"))
print("-" * width)

print(fmt.format("Apples", 280))
print(fmt.format("Gauva", 45))
print(fmt.format("Grapes", 140))
print(fmt.format("Oranges", 80))
print(fmt.format("Pineapple", 70))
print("-" * width)
