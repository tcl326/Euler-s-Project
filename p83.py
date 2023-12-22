
from typing import List
import heapq


def main(matrix: List[List[int]]):
    start = (0, 0)
    seen = set()
    queue = [(matrix[0][0], start)]
    while queue:
        score, (si, sj) = heapq.heappop(queue)
        seen.add((si, sj))
        print(si, sj)
        if si == len(matrix) - 1 and sj == len(matrix[0]) - 1:
            return score
        for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ni, nj = si + di, sj + dj
            if ni < 0 or ni >= len(matrix) or nj < 0 or nj >= len(matrix[0]) or (ni, nj) in seen:
                continue
            heapq.heappush(queue, (score + matrix[ni][nj], (ni, nj)))
    


if __name__ == "__main__":
    file_name = "0083_matrix.txt"
    matrix = []
    with open(file_name, "r") as f:
        line = f.readline()
        while line:
            matrix.append([int(l) for l in line.strip().split(",")])
            line = f.readline()

    print(main(matrix)) 