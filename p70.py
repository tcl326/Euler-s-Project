
import collections
import tqdm

from lib.primes import sieve_of_eratosthenes


primes = list(sieve_of_eratosthenes(10_000_000))
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


def main(n) -> int:
    res = 0
    min_quote = float('inf')
    for i in tqdm.tqdm(range(2, n)):
        ci = collections.Counter(str(i))
        n = totient_function(i)
        cn = collections.Counter(str(n))
        if ci == cn:
            if i / n < min_quote:
                min_quote = i / n
                res = i
    return res


if __name__ == "__main__":
    print(main(10_000_000))