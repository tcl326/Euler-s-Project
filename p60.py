from lib.primes import sieve_of_eratosthenes, miller_rabin_test

def main():
    primes = list(sieve_of_eratosthenes(50000))
    res = float('inf')
    for i in range(len(primes)):
        pi = primes[i]
        if pi > res:
            continue
        if pi == 2 or pi == 5:
            continue
        for j in range(i + 1, len(primes)):
            pj = primes[j]
            if pi + pj > res:
                continue
            if not miller_rabin_test(int(str(pi) + str(pj))) or not miller_rabin_test(int(str(pj) + str(pi))):
                continue
            for k in range(j + 1, len(primes)):
                pk = primes[k]
                if pi + pj + pk > res:
                    continue
                if (
                    not miller_rabin_test(int(str(pi) + str(pk)))
                    or not miller_rabin_test(int(str(pk) + str(pi)))
                    or not miller_rabin_test(int(str(pj) + str(pk)))
                    or not miller_rabin_test(int(str(pk) + str(pj)))
                ):
                    continue
                for l in range(k + 1, len(primes)):
                    pl = primes[l]
                    if pi + pj + pl + pk > res:
                        continue
                    if (
                        not miller_rabin_test(int(str(pi) + str(pl)))
                        or not miller_rabin_test(int(str(pl) + str(pi)))
                        or not miller_rabin_test(int(str(pj) + str(pl)))
                        or not miller_rabin_test(int(str(pl) + str(pj)))
                        or not miller_rabin_test(int(str(pk) + str(pl)))
                        or not miller_rabin_test(int(str(pl) + str(pk))) 
                    ):
                        continue
                    for m in range(l + 1, len(primes)):
                        pm = primes[m]
                        if pi + pj + pl + pk + pm > res:
                            continue
                        if (
                            not miller_rabin_test(int(str(pi) + str(pm)))
                            or not miller_rabin_test(int(str(pm) + str(pi)))
                            or not miller_rabin_test(int(str(pj) + str(pm)))
                            or not miller_rabin_test(int(str(pm) + str(pj)))
                            or not miller_rabin_test(int(str(pk) + str(pm)))
                            or not miller_rabin_test(int(str(pm) + str(pk)))
                            or not miller_rabin_test(int(str(pl) + str(pm)))
                            or not miller_rabin_test(int(str(pm) + str(pl))) 
                        ):
                            continue
                        res = min(res, pi + pj + pk + pl + pm)
    return res



if __name__ == "__main__":
    print(main())