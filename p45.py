import math

def get_hexagon_number(i: int) -> int:
    return i * (2 * i - 1)

def is_triangle_number(t: int) -> bool:
    """
    T_n = n * (n + 1) / 2
    => 0 = n ^ 2 + n - 2 * T_n
    => n = (-1 + math.sqrt(1 + 8 * T_n)) / 2 as n can only be positive
    """
    n = (-1 + math.sqrt(1 + 8 * t)) / 2
    return n.is_integer()

def is_pentagon_number(p: int) -> bool:
    """
    P_n = n * (3 * n - 1) / 2
    => 0 = 3 * n ^ 2 - n - 2 * P_n
    => n = (1 + math.sqrt(1 + 24 * P_n)) / 6 as n can only be positive
    """
    n = (1 + math.sqrt(1 + 24 * p)) / 6
    return n.is_integer()

def main():
    s = 144
    while True:
        h = get_hexagon_number(s)
        if is_triangle_number(h) and is_pentagon_number(h):
            return h
        s += 1


if __name__ == "__main__":
    print(main())
