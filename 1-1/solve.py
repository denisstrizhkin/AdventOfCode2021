with open("./input", mode="r", encoding="utf8") as f:
    lines = f.readlines()

measurments = list(map(int, lines))
previous = measurments.pop(0)
count = 0

for measurment in measurments:
    if measurment > previous:
        count += 1
    previous = measurment

with open("./answer", mode="w", encoding="utf8") as f:
    f.write(f"{count}\n")
