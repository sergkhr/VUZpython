import math


def main(z):
    if z < 141:
        return 35*(z**2 - z)**6
    elif 141 <= z < 209:
        return (z**3 - 1)**6
    elif z >= 209:
        return math.tan(98 * z**3)**5 + 20*math.exp(z**2/81 - 52*z**3 - 1)**2\
            + 1


a = int(input("Enter a number: "))
print(main(a))
