with open("./input", mode="r") as f:
    lines = f.readlines()

values = map(int, lines)
a = float("inf")
b = float("inf")
c = float("inf")
d = float("inf")
count = 0

for i, val in enumerate(values):
    match i % 4:
        case 0:
            a = val
            c += val
            d += val
            if c > b:
                count += 1
        case 1:
            a += val
            b = val
            d += val
            if d > c:
                count += 1
        case 2:
            a += val
            b += val
            c = val
            if a > d:
                count += 1
        case 3:
            b += val
            c += val
            d = val
            if b > a:
                count += 1

with open("./answer", mode="w") as f:
    f.write(f"{count}\n")
