def check(n: int):
    return sum_digits(str(n)) % 7 == 0

def sum_digits(n: str) -> int:
    if len(n) == 0:
        return 0
    return int(n[0]) + sum_digits(n[1:])