with open("./input", mode="r") as f:
    lines = f.readlines()

length = len(lines[0].strip())
count = len(lines)
one_rate = [0] * length
for line in lines:
    for i, _ in enumerate(one_rate):
        one_rate[i] += int(line[i])

gamma_bits = ["0"] * length
epsilon_bits = ["1"] * length
for i, _ in enumerate(one_rate):
    if one_rate[i] > count / 2:
        gamma_bits[i] = "1"
        epsilon_bits[i] = "0"

gamma = int("".join(gamma_bits), 2)
epsilon = int("".join(epsilon_bits), 2)

with open("./answer", mode="w") as f:
    f.write(f"{gamma * epsilon}\n")
