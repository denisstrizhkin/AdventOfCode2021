from __future__ import annotations
from collections import Counter
from itertools import groupby
import operator


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
    class FishMultiplier(Fish):
        def __init__(self, initial_state: int, multiplier: int = 1):
            super().__init__(initial_state)
            self.multiplier = multiplier

        def __str__(self) -> str:
            return super().__str__() + f"({self.multiplier})"

        def tick(self) -> Population.FishMultiplier | None:
            result = super().tick()
            if result:
                return Population.FishMultiplier(result.timer, self.multiplier)

    def __init__(self, initial_state: str):
        self.fishes = list(
            map(Population.FishMultiplier, map(int, initial_state.split(",")))
        )

    def __str__(self) -> str:
        return ",".join(map(str, self.fishes))

    def tick(self):
        new_fish = list()
        for fish in self.fishes:
            result = fish.tick()
            if result:
                new_fish.append(result)
        self.fishes += new_fish

        if self.count() > 100:

            def key_func(fish: Fish) -> int:
                return fish.timer

            groups = groupby(sorted(self.fishes, key=key_func), key_func)
            self.fishes = [
                Population.FishMultiplier(
                    state, sum(map(lambda f: f.multiplier, fishes))
                )
                for state, fishes in groups
            ]

    def count(self) -> int:
        return sum(map(lambda f: f.multiplier, self.fishes))


if __name__ == "__main__":
    with open("./input", mode="r") as f:
        lines = f.readlines()
    initial_state = lines[0].strip()
    population = Population(initial_state)

    for i in range(256):
        population.tick()

    answer = population.count()
    print(f"answer: {answer}")
    with open("./answer", mode="w") as f:
        f.write(f"{answer}\n")
