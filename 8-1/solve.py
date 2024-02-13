def count_occurances(output: str, digits: dict[int, str]) -> int:
    tokens = map("".join, map(sorted, output.split()))
    return sum(map(lambda t: t in digits.values(), tokens))


def anaylyze_input(input: str) -> dict[int, str]:
    tokens = input.split()
    digits: dict[int, str] = dict()

    count_patterns = {1: 2, 4: 4, 7: 3, 8: 7}
    for digit, count in count_patterns.items():
        digits[digit] = "".join(sorted([t for t in tokens if len(t) == count][0]))

    return digits


if __name__ == "__main__":
    with open("./input", mode="r") as f:
        lines = f.readlines()

    answer = 0
    for line in lines:
        (input, output) = line.strip().split(" | ")
        digits = anaylyze_input(input)
        answer += count_occurances(output, digits)

    print(f"answer: {answer}")
    with open("./answer", mode="w") as f:
        f.write(f"{answer}\n")
