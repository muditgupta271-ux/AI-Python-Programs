"""Generate the Fibonacci series using a loop."""


def fibonacci(terms):
    if terms < 0:
        raise ValueError("Number of terms cannot be negative.")
    sequence = []
    a, b = 0, 1
    for _ in range(terms):
        sequence.append(a)
        a, b = b, a + b
    return sequence


if __name__ == "__main__":
    try:
        count = int(input("Enter the number of terms: "))
        print("Fibonacci series:", *fibonacci(count))
    except ValueError as error:
        print(f"Invalid input: {error}")
