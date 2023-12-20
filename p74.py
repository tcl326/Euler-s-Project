from typing import List
import math
import tqdm

def get_digit_factorial_chain(n: int) -> List[int]:
    seen = set()
    chain = [n]
    def recurse(v: int):
        seen.add(v)
        r = 0
        while v:
            d = v % 10 
            v //= 10
            r += math.factorial(d)
        if r in seen:
            return
        chain.append(r)
        recurse(r)
    recurse(n)
    return chain

def main():
    r = 0
    for i in tqdm.tqdm(range(1, 1_000_000 + 1)):
        chain = get_digit_factorial_chain(i)
        # print(i, chain)
        if len(chain) == 60:
            r += 1
    return r



if __name__ == "__main__":
    print(main())
