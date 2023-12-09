
def main():
    targets = [1, 10 , 100, 1000, 10000, 100000, 1000000]
    c_target = targets[0]
    c_target_idx = 0
    res = 1
    c_start = 0
    c_end = 0
    for i in range(10 ** 6):
        c_end = len(str(i)) + c_start
        if c_target >= c_start and c_target < c_end:
            print(int(str(i)[c_target - c_start]))
            res *= int(str(i)[c_target - c_start])
            c_target_idx += 1
            if c_target_idx >= len(targets):
                return res
            c_target = targets[c_target_idx]
        c_start = c_end
    return res


if __name__ == "__main__":
    print(main())