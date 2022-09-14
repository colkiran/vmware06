
# emulate C style
format = "Welcome %s, what a %s player"
print(format)
values = ("Sachin", "superb")               # tuple
print(values)
print(format % values)
print("-" * 40)

format = "Welcome %s, your rating of %.3f, what a %s player"
print(format % ("Sachin", 4, "superb"))
print(format % ("Sachin", 4.8, "superb"))
print(format % ("Sachin", 4.8124, "superb"))
print(format % ("Sachin", 4.8987564, "superb"))
print("Welcome %s, your rating of %.3f, what a %s player" % ("Sachin", 4.897562, "superb"))

# emulate unix shell syntax
print("-" * 40)
from string import Template
tmpl = Template("Welcome $name, what a $adj player")
print(tmpl)
res = tmpl.substitute(name = "Sachin", adj = "superb")
print(f"res :{res}")

print("-" * 40)
# format string from python

print("Welcome {}, what a {} player for {}".format("Sachin", "superb", "India"))
print("Welcome {0}, what a {1} player for {2}".format("Sachin", "superb", "India"))
print("Welcome {1}, what a {2} player for {0}".format("India", "Sachin", "superb"))
print("Welcome {name}, what a {adj} player for {ctry}".format(ctry="India", name="Sachin", adj="superb"))
print("Welcome {name}, with a rating of {rating}, what a {adj} player for {ctry}".format(ctry="India", name="Sachin", adj="superb", rating=4))

print("Welcome {name}, with a rating of {rating:.2f}, what a {adj} player for {ctry}".format(ctry="India", name="Sachin", adj="superb", rating=4.89763))

print("-" * 40)
# interpolation
from math import pi, e
print(f"PI = {pi} and Euler's constant = {e}")
print("PI = {} and Euler's constant = {}".format(pi, e))
print("PI = {}, Euler's constant {} and magic_number = {magic}".format(pi, e, magic= 40585))
print("PI = {0}, Euler's constant {1} and magic_number = {magic}".format(pi, e, magic= 40585))


print("-" * 40)
full_name = ["Sachin", "Tendulkar"]
print("Mr. {name}".format(name = full_name))
print("Mr. {name[0]}".format(name = full_name))
print("Mr. {name[0]} {name[1]}".format(name = full_name))

print("-" * 40)
import math
print(__name__)         # name of the main function __main__
print(math.__name__)

print("the {mod.__name__} module gives the value of pi = {mod.pi} and eulers constant {mod.e}".format(mod=math))