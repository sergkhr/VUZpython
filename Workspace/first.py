import math


def main(y, x, z):
    up = 38 * math.asin(y**3 + x**2/96 + z)**6
    down = 15 * math.floor(67*x**2 - 22*y - z**3)**6
    right = x/26 - (y - z**2)**2
    if down == 0:
        return math.inf
    return up/down - right


print(main(0.78, 0.54, -0.39))
y = float(input())
x = float(input())
z = float(input())
print(main(y, x, z))
