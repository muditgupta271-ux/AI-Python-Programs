"""Calculate the factorial of a non-negative integer using recursion."""


def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    try:
        number = int(input("Enter a non-negative integer: "))
        print(f"Factorial of {number} is {factorial(number)}")
    except ValueError as error:
        print(f"Invalid input: {error}")
