
import sys

for pth in sys.path:
    print(pth)

from gurgaon import mymodule as m
from gurgaon.mymodule import Player

m.greet("Ravi Shastri")
print("-" * 40)

ply1 = Player("Dinesh Karthik", 37)
ply1.get_details()
