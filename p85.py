
import math


def rect_count(row: int, column: int) -> int:
    # count = 0
    # for i in range(row):
    #     for j in range(column):
    #         count += (row - i) * (column - j)
    # return count
    return row * ( row + 1 ) * column * (column + 1) / 4


def main(limit: int) -> int:
    res = float('inf')
    min_diff = float('inf')
    for n in range(int(math.sqrt(2 * limit)) + 1):
        for m in range(n,int(math.sqrt(2 * limit)) + 1):
            c = rect_count(n, m)
            if abs(c - limit) < min_diff:
                area = n * m
                print("min area:", area, "rects", c, min_diff)
                min_diff = abs(c - limit)
                res = area
    return res


if __name__ == "__main__":
    print(main(2_000_000))
    # print(rect_count(3, 2))