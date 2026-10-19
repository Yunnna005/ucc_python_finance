import math

def factorial():
    x = int(input("Enter a number: "))
    result = 1
    for i in range(1, x + 1):
        result *= i

    print("Product:", result)

factorial()


def factorial_short():
    x = int(input("Enter a number: "))
    print("Product:", math.factorial(x))

factorial_short()