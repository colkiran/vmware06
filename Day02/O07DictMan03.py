
# pop, popitem
print("pop".center(40, "-"))

player = {'name': 'Sachin', 'runs': 135, 'oppn': 'Srilanka', 'venue': 'Chepauk', 'age': 34, 'year': 2001}
print(f"player :{player}")

res = player.pop('oppn')
print(f"res :{res}")

print(f"player :{player}")

print("popitem".center(40, "-"))
player = {'name': 'Sachin', 'runs': 135, 'oppn': 'Srilanka', 'venue': 'Chepauk', 'age': 34, 'year': 2001}
print(f"player :{player}")

res = player.popitem()
print(f"res :{res}")

res = player.popitem()
print(f"res :{res}")

print(f"player :{player}")

print("update".center(40, "-"))

emp1 = {'ename': 'Jack', 'age': 34, 'dept': 'Finance', 'desig': 'MGR', 'loc': 'Blr'}
emp2 = {'ename': 'Tina', 'age': 30, 'dept': 'MKT', 'desig': 'BDM', 'sal': 75000}

print(f"emp1 :{emp1}")
print(f"emp2 :{emp2}")

# update emp1 with emp2's values
emp1.update(emp2)
print(f"emp1 :{emp1}")

print("clear".center(40, "-"))
emp1 = {'ename': 'Jack', 'age': 34, 'dept': 'Finance', 'desig': 'MGR', 'loc': 'Blr'}
print(f"emp1 :{emp1}")
emp1.clear()
print(f"emp1 :{emp1}")

print("copy".center(40, "-"))
d1 = {'empname': 'Jack', 'age': 32, 'desig': 'MGR'}
print(f"d1 before :{d1}")
d2 = d1                     # shallow copy
print(f"d2 before :{d2}")

d2['dept'] = "Finance"
d2['sal'] = 55000

print(f"d2 after :{d2}")
print(f"d1 after :{d1}")

print("-" * 40)
emp3 = {'ename': 'Jack', 'age': 34, 'dept': 'Finance', 'desig': 'MGR', 'loc': 'Blr'}
print(f"emp3 before :{emp3}")
emp4 = emp3.copy()
print(f"emp4 :{emp4}")

emp4['gender'] = 'male'
emp4['sal'] = 50000
print(f"emp4 after :{emp4}")
print(f"emp3 after :{emp3}")

print("-" * 40)
emp5 = {'ename': 'Jack', 'age': 34, 'dept': 'Finance', 'desig': {'ibm': 'trainee', 'tcs': 'TL', 'wipro': 'MGR'}, 'loc': 'Blr'}
print(f"emp5  before  :{emp5}")
emp6 = emp5.copy()
print(f"emp6 before  :{emp6}")

emp6['desig']['dell'] = 'PL'
emp6['desig']['cisco'] = 'PM'
print(f"emp6 after  :{emp6}")
print(f"emp5 after  :{emp5}")

print("-" * 40)
print("-" * 40)
emp7 = {'ename': 'Jack', 'age': 34, 'dept': 'Finance', 'desig': {'ibm': 'trainee', 'tcs': 'TL', 'wipro': 'MGR'}, 'loc': 'Blr'}
print(f"emp7 before  :{emp7}")
from copy import deepcopy
emp8 = deepcopy(emp7)
print(f"emp8 before  :{emp8}")

print("-" * 40)
emp8['desig']['dell'] = 'PL'
emp8['desig']['cisco'] = 'PM'
print(f"emp8 after  :{emp8}")
print(f"emp7 after  :{emp7}")