with open("./input", mode="r") as f:
    lines = f.readlines()


def filter_by_rating(nums, cmp, i):
    ones = list()
    zeros = list()
    for num in nums:
        if num[i] == "1":
            ones.append(num)
        else:
            zeros.append(num)

    return cmp(ones, zeros, i)


def find_rating(nums, cmp):
    rating = nums.copy()
    for i, _ in enumerate(nums[0]):
        rating = filter_by_rating(rating, cmp, i)
        if len(rating) == 1:
            return rating


def cmp_oxygen(a, b, i):
    if len(a) > len(b):
        return a

    if len(a) == len(b) and a[0][i] == "1":
        return a

    return b


def cmp_co2(a, b, i):
    if len(a) < len(b):
        return a

    if len(a) == len(b) and a[0][i] == "0":
        return a

    return b


lines = [line.strip() for line in lines]
oxygen_bits = find_rating(lines, cmp_oxygen)
co2_bits = find_rating(lines, cmp_co2)

oxygen = int("".join(oxygen_bits), 2)
co2 = int("".join(co2_bits), 2)

with open("./answer", mode="w") as f:
    f.write(f"{oxygen * co2}\n")
