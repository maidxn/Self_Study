numberOfRocks = int(input())
rocks = {}
for rock in range(numberOfRocks):
    new_rock = input()
    set_of_mineral = set(new_rock)
    for mineral in set_of_mineral:
        if mineral not in rocks.keys():
            rocks[mineral] = 1
        else:
            rocks[mineral] += 1
gemstones = 0
for item in rocks.values():
    if item == numberOfRocks:
        gemstones += 1
print(gemstones)
