from typing import List

def main(msg: List[str]):
    max_l = 0
    for i in range(26):
        for j in range(26):
            for k in range(26):
                decoded = []
                keys = [i + ord('a'), j + ord('a'), k + ord('a')]
                for l, m in enumerate(msg):
                    d = int(m) ^ keys[l % len(keys)]
                    if (d >= 32 and d <= 94) or (d >= 97 and d <= 124):
                        decoded.append(d)
                    else:
                        max_l = max(l, max_l)
                        break
                else:
                    return sum(decoded)
    print("max_l", max_l)
    return -1



if __name__ == "__main__":
    file_name = "0059_cipher.txt"
    with open(file_name, "r") as f:
        msg = f.readline().strip().split(",")
    print(msg)
    print(len(msg))
    print(main(msg))
