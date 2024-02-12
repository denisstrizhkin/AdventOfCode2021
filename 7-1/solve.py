import sys


def calc_fuel(positions: list[int], target: int) -> int:
    return sum(map(lambda pos: abs(pos - target), positions))


if __name__ == "__main__":
    with open("./input", mode="r") as f:
        lines = f.readlines()

    positions_str = lines[0].strip()
    positions = list(map(int, positions_str.split(",")))

    answer = sys.maxsize
    for fuel in range(min(positions), max(positions) + 1):
        answer = min(answer, calc_fuel(positions, fuel))

    print(f"answer: {answer}")
    with open("./answer", mode="w") as f:
        f.write(f"{answer}\n")
