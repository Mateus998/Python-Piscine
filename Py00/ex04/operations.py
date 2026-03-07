import sys


def print_operations(num1: int, num2: int) -> None:
    """
    Prints the operations between argumants. Sum, difference, product, quotient and remainder.
    If the division and remainder are by zero, an error message is shown on the value spot
    """
    labels = ["Sum:", "Difference:", "Product:", "Quotient:", "Remainder:"]
    values: list[str] = []
    values.append(str(num1 + num2))
    values.append(str(num1 - num2))
    values.append(str(num1 * num2))

    try:
        v = num1 / num2
        if isinstance(v, float):
            values.append(f"{v:.2f}")
        else:
            values.append(str(num1 / num2))
        v = num1 % num2
        if isinstance(v, float):
            values.append(f"{v:.2f}")
        else:
            values.append(str(num1 % num2))
            
    except ZeroDivisionError:
        values.append("ERROR (division by zero)")
        values.append("ERROR (modulo by zero)")

    # try:
    # except ZeroDivisionError:

    size_l = max(map(len, labels))
    size_v = max(len(s) for s in values)

    for l, v in zip(labels, values):
        print(f"{l:<{size_l}} {v:<{size_v}}")


def main():
    assert len(sys.argv) == 3, "Usage: python3 operations.py <number1> <number2>"
    
    try:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
        print_operations(num1, num2)
    except ValueError:
        raise SystemExit("Arguments are not integer")


if __name__ == "__main__":
    main()