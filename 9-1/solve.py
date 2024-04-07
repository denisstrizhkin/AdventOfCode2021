if __name__ == "__main__":
    heights: list[list[int]] = []

    with open("input") as f:
        lines = f.readlines()

    for line in lines:
        heights.append(list(map(int, line.strip())))

    sum = 0
    for i, row in enumerate(heights):
        for j, height in enumerate(row):
            if i > 0:
                if heights[i - 1][j] <= height:
                    continue
            if j > 0:
                if heights[i][j - 1] <= height:
                    continue
            if i < len(heights) - 1:
                if heights[i + 1][j] <= height:
                    continue
            if j < len(heights[0]) - 1:
                if heights[i][j + 1] <= height:
                    continue
            sum += height + 1

    print("answer:", sum)
    with open("output", mode="w") as f:
        f.write(f"{sum}\n")
