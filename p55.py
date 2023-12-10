
def is_palindrome(s: str) -> bool:
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True


def is_lychrel(n: int) -> bool:
    for _ in range(50):
        s = n + int(str(n)[::-1])
        if is_palindrome(str(s)):
            return False
        n = s
    return True


def main():
    res = 0
    for i in range(10_000):
        if is_lychrel(i):
            res += 1
    return res

if __name__ == "__main__":
    print(main())