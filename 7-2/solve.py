import sys


class FuelTracker:
    def __init__(self, posistions: list[int]):
        self.positions = positions.copy()
        self.min = min(self.positions)
        self.max = max(self.positions)
        self.progression = self.calc_progression()

    def calc_progression(self) -> list[int]:
        progression = [0] * (self.max - self.min + 1)
        for i in range(1, len(progression)):
            progression[i] = progression[i - 1] + i
        return progression

    def calc_fuel(self, target: int):
        return sum(map(lambda pos: self.progression[abs(pos - target)], positions))


if __name__ == "__main__":
    with open("./input", mode="r") as f:
        lines = f.readlines()

    positions_str = lines[0].strip()
    positions = list(map(int, positions_str.split(",")))

    fuel_tracker = FuelTracker(positions)
    answer = sys.maxsize
    for target in range(fuel_tracker.min, fuel_tracker.max + 1):
        answer = min(answer, fuel_tracker.calc_fuel(target))

    print(f"answer: {answer}")
    with open("./answer", mode="w") as f:
        f.write(f"{answer}\n")
