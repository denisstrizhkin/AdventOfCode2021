with open("./input", mode="r") as f:
    lines = f.readlines()

aim = 0
x = 0
y = 0
for line in lines:
    tokens = line.strip().split()
    cmd = tokens[0]
    val = int(tokens[1])

    match cmd:
        case "forward":
            x += val
            y += val * aim
        case "down":
            aim += val
        case "up":
            aim -= val

with open("./answer", mode="w") as f:
    f.write(f"{x * y}\n")
