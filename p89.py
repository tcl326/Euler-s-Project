
from typing import List

from lib import roman


def optimize(numeral: str) -> str:
    return roman.to_numeral(roman.to_digit(numeral))


def main(numerals: List[str]) -> int:
    r = 0
    for num in numerals:
        r += len(num) - len(optimize(num))
    return r


if __name__ == "__main__":
    file_name = "0089_roman.txt"
    numerals = []
    with open(file_name, "r") as f:
        line = f.readline().strip()
        while line:
            numerals.append(line)
            line = f.readline().strip()
    
    print(main(numerals))
