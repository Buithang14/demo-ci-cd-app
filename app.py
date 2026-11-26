def add(a: int, b: int) -> int:
    return a + b

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Khong the chia cho 0")
    return a / b

if __name__ == "__main__":
    print("Demo App dang chay! 2 + 3 =", add(2, 3))