

value = {
    "I": 1,
    "IV": 4,
    "V": 5,
    "IX": 9,
    "X": 10,
    "XL": 40,
    "L": 50,
    "XC": 90,
    "C": 100,
    "CD": 400,
    "D": 500,
    "CM": 900,
    "M": 1000,
}


def to_digit(numeral: str) -> int:
    d = 0
    i = 0
    while i < len(numeral):
        if numeral[i] not in value:
            raise ValueError(f"Contains invalid letter {numeral[i]}")
        if i + 1 < len(numeral) and value[numeral[i]] < value[numeral[i + 1]]:
            d += value[numeral[i + 1]] - value[numeral[i]]
            i += 2
        else:
            d += value[numeral[i]]
            i += 1
    return d


def to_numeral(digit: int) -> str:
    r = []
    while digit > 0:
        for num, val in reversed(value.items()):
            if digit >= val:
                r.append(num)
                digit -= val
                break
    return "".join(r)


if __name__ == "__main__":
    print(to_digit("MCCCCCCVI"))
    print(to_digit("MDCVI"))
    print(to_numeral(to_digit("MCCCCCCVI")))
