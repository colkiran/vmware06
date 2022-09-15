
print("keys".center(40, "-"))
player = {'name': 'Sachin', 'runs': 135, 'oppn': 'Srilanka', 'venue': 'Chepauk', 'age': 34, 'year': 2001}
print(f"player :{player}")

k = player.keys()
print(f"k :{k}")
print(type(k))

print("-" * 40)
for k in player.keys():
    print(k + " => " + str(player[k]))

print("values".center(40, "-"))
player = {'name': 'Sachin', 'runs': 135, 'oppn': 'Srilanka', 'venue': 'Chepauk', 'age': 34, 'year': 2001}
print(f"player :{player}")

v = player.values()
print(f"v :{v}")
print(type(v))

print("items".center(40, "-"))

emp = {
    'emp1':{'ename': 'Jack', 'age':34, 'dept': 'Finance', 'desig': 'MGR', 'loc': 'Blr', 'sal': 98500},
    'emp2':{'ename': 'Tina', 'age':30, 'dept': 'MKT', 'desig': 'BDM', 'loc': 'Che', 'sal': 75000},
    'emp3':{'ename': 'Tom', 'age': 28, 'dept': 'IT', 'desig': 'TL', 'loc': 'Hyd', 'sal': 85000}
}

print(f"emp :{emp}")

print("-" * 40)

print(f"emp1 :{emp['emp1']}")

print("-" * 40)

print(f"emp2 :{emp['emp2']}")

print("-" * 40)

print(f"emp3 :{emp['emp3']}")

print("-" * 40)
for ky, info in emp.items():
    print(ky)
    print("-----")
    for k, v in info.items():
        print(k, "=>", v)
    print("-" * 40)

print("from keys".center(40, "-"))
# convert a list into a dictionary -> elements of the list will become the keys of the dictionary
cities = ['blr', 'che', 'mum', 'del', 'hyd', 'kol']
res1 = dict.fromkeys(cities)
print(f"res1 :{res1}")

res2 = dict.fromkeys(cities, 20)
print(f"res2 :{res2}")

print("set default".center(40, "-"))
# used to add new key value pair into the dictionary
emp1 ={'ename': 'Jack', 'age':34, 'dept': 'Finance', 'desig': 'MGR', 'loc': 'Blr', 'sal': 98500}
print(f"emp1 :{emp1}")

emp1.setdefault("age", 36)
emp1.setdefault('gender', "Male")
emp1.setdefault('desig', "GM")
emp1.setdefault('empid', 'emp25299')

print(f"emp1 :{emp1}")
