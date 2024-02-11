with open("./input", mode="r") as f:
    lines = f.readlines()

x = 0
y = 0
for line in lines:
    tokens = line.strip().split()
    cmd = tokens[0]
    val = int(tokens[1])

    match cmd:
        case "forward":
            x += val
        case "down":
            y += val
        case "up":
            y -= val

with open("./answer", mode="w") as f:
    f.write(f"{x * y}\n")
