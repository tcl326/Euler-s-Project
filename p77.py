
from lib.primes import sieve_of_eratosthenes

def main(n: int) -> int:
    seen = {}
    primes = list(sieve_of_eratosthenes(1_000_000))

    def recurse(v: int, m: int):
        if v < 0:
            return 0
        if v == 0:
            return 1
        if (v, m) in seen:
            return seen[(v, m)]
        r = 0
        for p in primes:
            if p > m:
                break
            r += recurse(v - p, min(v - p, p))
        seen[(v, m)] = r
        return r
    
    for i in range(4, n + 1):
        result = recurse(i, i)
        if result > n:
            print(seen)
            return (i, result)
    return result



if __name__ == "__main__":
    print(main(5_000))
