from typing import Set, Dict, Iterable, Tuple
import collections

def connections(attempt: str) -> Iterable[Tuple[str, str]]:
    l = len(attempt)
    for i in range(l - 1):
        for j in range(i + 1, l):
            yield attempt[i], attempt[j]


def make_graph(pass_code_set: Set[str]) -> Dict[str, Set[str]]:
    graph = collections.defaultdict(set)
    for attempt in pass_code_set:
        for a, b in connections(attempt):
            graph[a].add(b)
    return graph


def main(pass_code_set) -> str:
    graph = make_graph(pass_code_set)
    num_set = set()
    for p in pass_code_set:
        for d in p:
            num_set.add(d)
    candidates = []
    for start in graph:
        queue = collections.deque([(start, [start])])
        while queue:
            to_break = False
            curr, path = queue.popleft()
            neighbours = graph.get(curr, [])
            for n in neighbours:
                n_p = path + [n]
                if num_set == set(n_p):
                    candidates.append((len(n_p), n_p))
                    to_break = True
                    break
                queue.append((n, n_p))
            if to_break:
                break
    return "".join(sorted(candidates)[0][1])
    


if __name__ == "__main__":
    file_name = "0079_keylog.txt"
    pass_codes = []
    with open(file_name, "r") as f:
        line = f.readline()
        while line:
            pass_codes.append(line.strip())
            line = f.readline()
    
    print(main(set(pass_codes)))