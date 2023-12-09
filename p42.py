triangle_values = set()
curr_max_triangle_values = 0
curr_n = 0


def get_word_value(word: str) -> int:
    res = 0
    for w in word:
        res += ord(w) - ord("A") + 1
    return res


def is_triangle(value: int) -> bool:
    global curr_max_triangle_values, curr_n
    if value <= curr_max_triangle_values:
        if value in triangle_values:
            return True
        return False
    
    while value > curr_max_triangle_values:
        curr_n += 1
        curr_max_triangle_values = curr_n * (curr_n + 1) / 2
        triangle_values.add(curr_max_triangle_values)
        if value == curr_max_triangle_values:
            return True
    return False


if __name__ == "__main__":
    file_name = "0042_words.txt"

    with open(file_name, "r") as f:
        line = f.readline().strip()
        words = [w.strip('"') for w in line.split(",")]
    
    res = 0
    for w in words:
        if is_triangle(get_word_value(w)):
            res += 1
    print(res)