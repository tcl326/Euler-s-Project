
from lib.primes import sieve_of_eratosthenes
import math



def main(limit: int) -> int:
    primes = list(sieve_of_eratosthenes(int(math.sqrt(limit)) * 2 + 1))
    count = 0
    a = 0
    b = 0
    c = 0

    a4 = primes[a] ** 4
    b3 = primes[b] ** 3
    c2 = primes[c] ** 2
    seen = set()

    while a4 < limit:
        while a4 + b3 < limit:
            while a4 + b3 + c2 < limit:
                # print(c2, b3, a4)
                seen.add(a4 + b3 + c2)
                c += 1
                c2 = primes[c] ** 2
            c = 0
            b += 1
            c2 = primes[c] ** 2
            b3 = primes[b] ** 3
        c = 0
        b = 0
        a += 1
        c2 = primes[c] ** 2
        b3 = primes[b] ** 3
        a4 = primes[a] ** 4
    
    return len(seen) 



if __name__ == "__main__":
    print(main(50_000_000))