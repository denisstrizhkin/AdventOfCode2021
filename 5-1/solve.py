import itertools


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"


class Segment:
    def __init__(self, start: Point, end: Point):
        self.start = start
        self.end = end

    def __str__(self) -> str:
        return f"{self.start} -> {self.end}"


class Field:
    def __init__(self, width: int, height: int):
        self.height = height
        self.width = width
        self.field = [[0] * width for _ in range(height)]

    def __str__(self) -> str:
        s = f"{self.width} x {self.height}\n"
        for row in self.field:
            s += "".join(map(str, row)) + "\n"
        return s

    def plot_vent(self, segment: Segment):
        start = segment.start
        end = segment.end

        if start.x == end.x:
            if start.y > end.y:
                start, end = end, start
            p = start.y
            while p <= end.y:
                self.field[p][start.x] += 1
                p += 1

        if start.y == end.y:
            if start.x > end.x:
                start, end = end, start
            p = start.x
            while p <= end.x:
                self.field[start.y][p] += 1
                p += 1

    def count_overlapping(self) -> int:
        return sum(map(lambda val: val >= 2, itertools.chain.from_iterable(self.field)))


def point_from_str(s: str) -> Point:
    tokens = tuple(map(int, s.split(",")))
    return Point(*tokens)


if __name__ == "__main__":
    with open("./input", mode="r") as f:
        lines = f.readlines()

    width = 0
    height = 0
    segments: list[Segment] = list()

    for line in lines:
        tokens = line.strip().split(" -> ")

        start = point_from_str(tokens[0])
        end = point_from_str(tokens[1])

        width = max(width, max(start.x, end.x))
        height = max(height, max(start.y, end.y))

        segment = Segment(start, end)
        segments.append(segment)

    field = Field(width + 1, height + 1)
    for segment in segments:
        field.plot_vent(segment)

    answer = field.count_overlapping()
    print(f"answer: {answer}")
    with open("./answer", mode="w") as f:
        write = f.write(f"{answer}\n")
