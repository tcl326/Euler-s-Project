from lib.primes import sieve_of_eratosthenes
import collections
import tqdm

primes = list(sieve_of_eratosthenes(1_000_000))
prime_set = set(primes)

def totient_function(n: int) -> int:
    factorization = collections.defaultdict(int)
    for p in primes:
        if n == 1:
            break
        if n in prime_set:
            factorization[n] += 1
            n //= n
            break
        while n % p == 0:
            factorization[p] += 1
            n //= p
    r = 1
    for p, k in factorization.items():
        r *= p ** (k - 1) * (p - 1)
    return r


def main(n: int) -> int:
    f_1 = 2
    for i in range(2, n + 1):
        f_n = f_1 + totient_function(i)
        f_1 = f_n
    return f_n - 2


if __name__ == "__main__":
    print(main(1_000_000))

