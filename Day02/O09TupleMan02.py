
from collections import namedtuple

nmdTpl = namedtuple("Product", "pname cat price qty")
prod = nmdTpl(pname="Pepsi", cat="Baverage", price=85, qty=5)
print(f"prod :{prod}")

print("-" * 40)
print(f"Prod Name :{prod.pname}")
print(f"Category  :{prod.cat}")
print(f"Price     :{prod.price}")
print(f"Quantity  :{prod.qty}")

# prod.qty = 10