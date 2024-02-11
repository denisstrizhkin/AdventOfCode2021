with open("./input", mode="r") as f:
    lines = f.readlines()

codes = lines.pop(0).strip().split(",")
codes = list(map(int, codes))


class Board:
    def __init__(self, nums):
        self.nums = nums
        self.hits = [[False] * 5 for _ in range(5)]
        self.is_winner = False
        self.score = 0

    def __str__(self):
        s = ""
        for i, row in enumerate(self.nums):
            line = []
            for j, num in enumerate(row):
                if self.hits[i][j]:
                    line.append(f"[{num:2}]")
                else:
                    line.append(f" {num:2} ")
            s += " ".join(line) + "\n"
        return s

    def check_hits(self, code):
        for i, row in enumerate(self.nums):
            for j, num in enumerate(row):
                if num == code:
                    self.hits[i][j] = True
        self.check_winner()

    def check_column(self, j):
        for row in self.hits:
            if not row[j]:
                return False
        return True

    def check_winner(self):
        for i, row in enumerate(self.hits):
            if all(row) or self.check_column(i):
                self.is_winner = True
                self.calc_score()
                return

    def calc_score(self):
        for i, row in enumerate(self.hits):
            for j, hit in enumerate(row):
                if not hit:
                    self.score += self.nums[i][j]


def read_nums():
    lines.pop(0)
    nums = list()
    for i in range(5):
        row = lines.pop(0).strip().split()
        nums.append(list(map(int, row)))
    return nums


boards = list()
while lines:
    nums = read_nums()
    boards.append(Board(nums))


def check_boards(boards, code):
    left = boards.copy()
    winners = list()
    for board in boards:
        board.check_hits(code)
        if board.is_winner:
            left.remove(board)
            winners.append((board, code))
    return (winners, left)


left = boards.copy()
winners = []
for code in codes:
    won, left = check_boards(left, code)
    winners += won

(winner, code) = winners[-1]
with open("./answer", mode="w") as f:
    f.write(f"{winner.score * code}\n")
