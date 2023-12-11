
def main():
    res = 0
    for i in range(1, 9 + 1):
        for j in range(1, 100 + 1):
            if len(str(i ** j)) == j:
                print(i ** j)
                res += 1
    return res


if __name__ == "__main__":
    print(main())