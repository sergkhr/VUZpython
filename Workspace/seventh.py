import math


def main(x):
    r1 = x & 0b11
    r2 = x & 0b11111000
    r2 = r2 >> 3
    res = r1


a = 0xa9
print(main(a))
print (0b10101001)
print (0b01101010)