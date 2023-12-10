import math
import itertools

a = []

def sieve_of_eratosthenes(max_n: int = 100000000):
    global a
    a = [True] * max_n
    for i in range(2, int(math.sqrt(max_n)) + 1):
        if a[i]:
            for j in range(i ** 2, max_n, i):
                a[j] = False
            yield i
    for i in range(int(math.sqrt(max_n)) + 1, max_n):
        if a[i]:
            yield i

def find_all(s: str, sub: str):
    start = 0
    while True:
        start = s.find(sub, start)
        if start == -1:
            return
        yield start
        start += len(sub)

def main():
    for prime in sieve_of_eratosthenes():
        prime_str = str(prime)
        if "9" in prime_str:
            print(prime_str)
            indices = list(find_all(prime_str, "9"))
            for c in itertools.chain(*[itertools.combinations(indices, l + 1) for l in range(len(indices))]):
                prime_list = list(prime_str)
                family_size = 1
                smallest_prime = prime
                for i in range(9):
                    for ic in c:
                        prime_list[ic] = str(i)
                    n_p = int("".join(prime_list))
                    if a[n_p]:
                        family_size += 1
                        smallest_prime = min(smallest_prime, n_p)
                if family_size == 8:
                    return prime, smallest_prime

if __name__ == "__main__":
    print(main())