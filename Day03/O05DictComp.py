
players = {
    'sachin': [300, 345, 225, 205, 285],
    'sourav': [200, 305, 330, 405, 150],
    'rahul': [145, 230, 298, 360, 215],
    'sehwag': [120, 150, 405, 380, 450],
    'yuvraj': [185, 205, 230, 120, 160],
    'laxman': [105, 185, 250, 385, 180]
}

print(f"players :{players}")
print("-" * 40)

score = [(k, "=>", v) for k, v in players.items()]
print(f"score :{score}")

print("-" * 40)
print(f"sachin :{players['sachin']}")

print("-" * 40)
print(f"sachin :{sum(players['sachin'])}")

print("-" * 40)
score = {k: v for k, v in players.items()}
print(f"score :{score}")

print("-" * 40)
score = {k: sum(v) for k, v in players.items()}
print(f"score :{score}")

print("-" * 40)
score = {k: (lambda score: sum(score) / len(score))(v) for k, v in players.items()}
print(f"score :{score}")

print("-" * 40)
basic = [{x :(lambda par: "Mr." + par)("Sachin {}".format(x))} for x in range(1, 6)]
print(f"basic :{basic}")

print("-" * 40)
plyr_score = [score for score in players.values()]
print(plyr_score)

print("-" * 40)
plyr_score = [scr for score in players.values() for scr in score]
print(plyr_score)

print("-" * 40)
plyr_score = [scr for score in players.values() for scr in score if scr >= 200]
print(plyr_score)

print("-" * 40)
# name- [scores >= 200]
plyr_score = {name: [scr for scr in score if scr >= 200] for name, score in players.items()}
print(plyr_score)
