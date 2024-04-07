def decipher(output: str, digits: dict[int, set[str]]) -> int:
    result = ""
    for pattern in map(set, output.split()):
        for number, number_pattern in digits.items():
            if pattern == number_pattern:
                result += str(number)
    return int(result)


def anaylyze_input(input: str) -> dict[int, set[str]]:
    tokens = input.split()
    digits: dict[int, set[str]] = dict()

    count_patterns = {1: 2, 4: 4, 7: 3, 8: 7}
    for digit, count in count_patterns.items():
        digits[digit] = set(sorted([t for t in tokens if len(t) == count][0]))

    patterns = list(map(set, map(sorted, tokens)))
    for digit in digits.values():
        patterns.remove(digit)

    for pattern in patterns:
        if len(pattern) == 5 and pattern.issuperset(digits[7]):
            digits[3] = pattern
    patterns.remove(digits[3])

    for pattern in patterns:
        if pattern.issuperset(digits[3]):
            digits[9] = pattern
    patterns.remove(digits[9])

    bottom_left = list(digits[8] - digits[9])[0]
    for pattern in patterns:
        if len(pattern) == 5:
            if bottom_left in pattern:
                digits[2] = pattern
            else:
                digits[5] = pattern
    patterns.remove(digits[2])
    patterns.remove(digits[5])

    for pattern in patterns:
        if pattern.issuperset(digits[5]):
            digits[6] = pattern
        else:
            digits[0] = pattern

    return digits


if __name__ == "__main__":
    with open("./input", mode="r") as f:
        lines = f.readlines()

    answer = 0
    for line in lines:
        (input, output) = line.strip().split(" | ")
        digits = anaylyze_input(input)
        number = decipher(output, digits)
        answer += number

    print(f"answer: {answer}")
    with open("./answer", mode="w") as f:
        f.write(f"{answer}\n")
