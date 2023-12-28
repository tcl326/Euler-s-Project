

def is_right_angle(p1, p2, p3):
    a = (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2
    b = (p3[0] - p2[0]) ** 2 + (p3[1] - p2[1]) ** 2
    c = (p3[0] - p1[0]) ** 2 + (p3[1] - p1[1]) ** 2

    return (a > 0 and b > 0 and c > 0) and ( a == (b + c) or b == ( a + c ) or c == ( a + b))


def main(limit: int) -> int:
    seen = set()
    for x1 in range(limit + 1):
        for y1 in range(limit + 1):
            for x2 in range(limit + 1):
                for y2 in range(limit + 1):
                    if x1 == x2 and y1 == y2:
                        continue
                    if is_right_angle((0, 0), (x1, y1), (x2, y2)):
                        seen.add(tuple(sorted([(x1, y1), (x2, y2)])))
    return len(seen)


if __name__ == "__main__":
    print(main(2))