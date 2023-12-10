from lib.primes import is_prime


def spiral_diagonal_number():
    start = 1
    diff = 2
    i = 0
    while True:
        yield start, diff
        i += 1
        start += diff
        if i % 4 == 0:
            diff += 2


def main():
    all_diagonal_count = 0
    all_diagonal_prime = 0
    for i, d in spiral_diagonal_number():
        all_diagonal_count += 1
        if is_prime(i):
            all_diagonal_prime += 1
        print(all_diagonal_prime / all_diagonal_count)
        if i > 10 and all_diagonal_prime / all_diagonal_count < 0.1:
            return d - 1


if __name__ == "__main__":
    print(main())