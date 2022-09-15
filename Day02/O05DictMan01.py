
d1 = dict()
print(f"d1 :{d1}")
print(type(d1))

print("-" * 40)
d2 = {1 :"a", 2: 'b', 3: 'c', 4: 'd'}
print(f"d2 :{d2}")
print(type(d2))

print("-" * 40)
d3 = dict([('name', 'sachin'), ('runs', 85),('oppn', 'Aus'), ('venue', 'Gabba')])
print(f"d3 : {d3}")
print(type(d3))

print("-" * 40)
d4 = dict(name='rahul', runs=75, oppn='SA', venue='Durban')
print(f"d4 :{d4}")
print(type(d4))

print("-" * 40)
#create a dictionary and read from it
player = {'name': 'Sachin', 'runs': 125, 'oppn': 'Srilanka', 'venue': 'gale'}
print(f"Name :{player['name']}")
print(f"Runs :{player['runs']}")

print("-" * 40)
for x in player:
    print(x, "=>",player[x])
print()

# modify -> add new key and values

print(f"player :{player}")

player['age'] = 34
player['year'] = 2001
player['venue'] = 'Chepauk'
player['runs'] = 135

print(f"player :{player}")

# delete
del player['year']
del player['venue']

print(f"player :{player}")

print("-" * 40)

print(player.get('runs', "Invalid key, Please enter a valid key"))
print(player.get('venue', "Invalid key, Please enter a valid key"))

print("-" * 40)
print(dir(player))



