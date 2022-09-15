"""
sort        -> will sort the original list
sorted      -> take a copy of the list and sorts it, original list will remain the same
"""


l1 = [10, 5, 9, 2, 1, 8, 3, 6, 4, 7]
print(f"l1 :{l1}")

res_asc = sorted(l1)
print(f"res_asc :{res_asc}")

l1.sort(reverse=True)       # sort in desc
print(f"l1 desc :{l1}")

print("-" * 40)
l1 = [10,'zebra', 'apple', 5, 'yellow', 'blue', 9, 'white', 'green',2,  'violet', 'pink', 1, 'maroon', 'orange', 8, 'cat', 'xray', 3, 'dog', 'unique',6, 4, 7, 19, 175, 1345, 26, 234, 2198]

print(f"l1 :{l1}")
print("-" * 40)
print("-" * 40)

res_asc = sorted(l1, key=ascii)
print(f"res_asc :{res_asc}")

print("-" * 40)

cities = ['kanyakumari', 'bangalore', 'delhi', 'thiruvananthapuram', 'ooty', 'hyderabad', 'mumbai', 'vishakapatnam', 'mysore', 'madurai', 'chennai']
print(f"cities :{cities}")

print("-" * 40)
print("-" * 40)
res_asc = sorted(cities, key=len)
res_dsc = sorted(cities, key=len, reverse=True)

print(f"res_asc :{res_asc}")

print("-" * 40)
print("-" * 40)

print(f"res_dsc :{res_dsc}")

print("-" * 40)
print("-" * 40)
months = ['dec', 'aug', 'apr', 'jul', 'jun', 'oct', 'mar', 'nov', 'jan', 'may', 'feb', 'sep']
# sort these months
from calendar import month_name
print(f"month_name :{list(month_name)}")
print(f"months :{months}")

def month_sort(mon):
    l = []
    for m in list(month_name):
        l.append(m[0:3].lower())
    if mon in l:
        return l.index(mon)

res_asc = sorted(months, key=month_sort)
print("-" * 40)
print(f"res_asc :{res_asc}")
