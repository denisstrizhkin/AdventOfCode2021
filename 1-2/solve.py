with open("./input", mode="r") as f:
    lines = f.readlines()

values = list(map(int, lines))
a, b, c, d = 0, 0, 0, 0
count = 0

for i, val in enumerate(values[:4]):
    match i % 4:
        case 0:
            a = val
        case 1:
            a += val
            b += val
        case 2:
            a += val
            b += val
            c = val
        case 3:
            b += val
            c += val
            d = val
            if b > a:
                count += 1

for i, val in enumerate(values[4:]):
    match i % 4:
        case 0:
            a = val
            c += val
            d += val
            if c > b:
                count += 1
                print(b, c)
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
