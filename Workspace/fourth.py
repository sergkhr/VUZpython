import math


def main(n):
    if n == 0:
        return -0.16
    elif n >= 1:
        return main(n-1) - main(n-1)**3 - 0.04


n = int(input("Enter n: "))
print(main(n))
