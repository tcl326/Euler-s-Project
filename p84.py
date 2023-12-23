from typing import Tuple
import random
import functools
import collections


board = [
    "GO", "A1", "CC1", "A2", "T1", "R1", "B1", "CH1", "B2", "B3",
    "JAIL", "C1", "U1", "C2", "C3", "R2", "D1", "CC2", "D2", "D3",
    "FP", "E1", "CH2", "E2", "E3", "R3", "F1", "F2", "U2", "F3",
    "G2J", "G1", "G2", "CC3", "G3", "R4", "CH3", "H1", "T2", "H2",
]

def to_jail() -> str:
    return "JAIL"

def to_go() -> str:
    return "GO"

def community_chest() -> str:
    r = random.randint(1, 16)
    if r == 1:
        return to_jail()
    if r == 2:
        return to_go()
    return None

def chance(n) -> str:
    r = random.randint(1, 16)
    if r == 1:
        return "GO"
    elif r == 2:
        return "JAIL"
    elif r == 3:
        return "C1"
    elif r == 4:
        return "E3"
    elif r == 5:
        return "H2"
    elif r == 6:
        return "R1"
    elif r == 7 or r == 8:
        if n == 1:
            return "R2"
        if n == 2:
            return "R3"
        if n == 3:
            return "R1"
    elif r == 9:
        if n == 1:
            return "U1"
        if n == 2:
            return "U2"
        if n == 3:
            return "U1"
    elif r == 10:
        if n == 1:
            return "T1"
        if n == 2:
            return "D3"
        if n == 3:
            return "CC3"
    return None


special = {
    "G2J": to_jail,
    "CC1": community_chest,
    "CC2": community_chest,
    "CC3": community_chest,
    "CH1": functools.partial(chance, 1),
    "CH2": functools.partial(chance, 2),
    "CH3": functools.partial(chance, 3)
}

def roll_dice(side) -> Tuple[int, int]:
    return random.randint(1, side), random.randint(1, side)


def main(side: int) -> str:
    mapping = {
        tile: idx for idx, tile in enumerate(board)
    }
    counter = collections.Counter()
    def simulate(steps):
        current = "GO"
        for i in range(steps):
            counter[current] += 1
            r1, r2 = roll_dice(side)
            s = r1 + r2
            c = mapping[current]
            next_tile = board[(c + s) % len(board)]
            if next_tile in special:
                potential = special[next_tile]()
                if potential is not None:
                    next_tile = potential
            current = next_tile
    
    simulate(1_000_000)
    r = []
    for tile, c in counter.most_common(3):
        r.append(mapping[tile])
    return r





if __name__ == "__main__":
    print(main(4))