from __future__ import annotations


class Fish:
    def __init__(self, initial_state: int):
        self.timer = initial_state

    def __str__(self) -> str:
        return str(self.timer)

    def tick(self) -> Fish | None:
        if self.timer == 0:
            self.timer = 6
            return Fish(8)

        self.timer -= 1
        return None


class Population:
    def __init__(self, initial_state: str):
        self.fishes = list(map(Fish, map(int, initial_state.split(","))))

    def __str__(self) -> str:
        return ",".join(map(str, self.fishes))

    def tick(self):
        new_fish = list()
        for fish in self.fishes:
            result = fish.tick()
            if result:
                new_fish.append(result)
        self.fishes += new_fish

    def count(self) -> int:
        return len(self.fishes)


if __name__ == "__main__":
    with open("./input", mode="r") as f:
        lines = f.readlines()
    initial_state = lines[0].strip()
    population = Population(initial_state)

    for i in range(80):
        population.tick()

    answer = population.count()
    print(f"answer: {answer}")
    with open("./answer", mode="w") as f:
        f.write(f"{answer}\n")
