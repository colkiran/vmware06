
import sys

sys.path.append("C:/Delhi")

for x in sys.path:
    print(x)

from gurgaon import mymodule as m
from gurgaon.mymodule import Player

m.greet("Sunil Gavaskar")
print("-" * 40)

ply1 = Player("Rohit Sharma", 34)
ply1.get_details()
