
from typing import List
import heapq

def main(matrix: List[List[int]]) -> int:

    def dikstra(start):
        si, sj = start
        queue = [(matrix[si][sj], (si, sj))]
        seen = set()
        while queue:
            score, (i, j) = heapq.heappop(queue)
            if j == len(matrix[0]) - 1:
                return score
            seen.add((i, j))
            for di, dj in [(-1, 0), (1, 0), (0, 1)]:
                ni, nj = di + i, dj + j
                if ni < 0 or ni >= len(matrix) or nj < 0 or nj >= len(matrix[0]) or (ni, nj) in seen:
                    continue
                heapq.heappush(queue, (score + matrix[ni][nj], (ni, nj)))
        return float('inf')
    
    r = float('inf')
    for i in range(len(matrix)):
        r = min(r, dikstra((i, 0)))
        print(r)
    return r


if __name__ == "__main__":
    file_name = "0082_matrix.txt"
    matrix = []
    with open(file_name, "r") as f:
        line = f.readline()
        while line:
            matrix.append([int(l) for l in line.strip().split(",")])
            line = f.readline()
    
    print(main(matrix))
