def calc_answer(basin_sizes):
    if basin_sizes[-1] == 0:
        basin_sizes.pop()

    if len(basin_sizes) == 0:
        return 0

    result = 1
    basin_sizes = sorted(basin_sizes, reverse=True)
    for i in range(0, min(3, len(basin_sizes))):
        result *= basin_sizes[i]

    return result


if __name__ == "__main__":
    heights: list[list[int]] = []
    visited: list[list[bool]] = []

    with open("input") as f:
        lines = f.readlines()

    for line in lines:
        heights.append(list(map(int, line.strip())))
        visited.append([False] * len(heights[-1]))

    basin_sizes: list[int] = []
    visit_queue: list[tuple[int, int]] = []
    count = len(heights) * len(heights[0])

    def set_visited(i: int, j: int) -> int:
        visited[i][j] = True
        return count - 1

    while count > 0:
        if len(visit_queue) == 0:
            for i, row in enumerate(visited):
                is_break = False
                for j, visit_status in enumerate(row):
                    if visit_status == False:
                        visit_queue.append((i, j))
                        basin_sizes.append(0)
                        is_break = True
                        break
                if is_break:
                    break

        i, j = visit_queue.pop()
        count = set_visited(i, j)
        if heights[i][j] != 9:
            basin_sizes[-1] += 1

        def check_next(i: int, j: int) -> int:
            if heights[i][j] == 9:
                return set_visited(i, j)

            if (i, j) not in visit_queue:
                visit_queue.append((i, j))
            return count

        if i > 0:
            if visited[i - 1][j] == False:
                count = check_next(i - 1, j)
        if j > 0:
            if visited[i][j - 1] == False:
                count = check_next(i, j - 1)
        if i < len(heights) - 1:
            if visited[i + 1][j] == False:
                count = check_next(i + 1, j)
        if j < len(heights[0]) - 1:
            if visited[i][j + 1] == False:
                count = check_next(i, j + 1)

    answer = calc_answer(basin_sizes)
    print("answer:", answer)
    with open("output", mode="w") as f:
        f.write(f"{answer}\n")
