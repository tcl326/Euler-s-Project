
def main(a, b) -> int:
    seq = set()
    for i in range(2, a + 1):
        for j in range(2, b + 1):
            seq.add(i ** j)
            seq.add(j ** i)
    return len(seq)

if __name__ == "__main__":
    print(main(100, 100))