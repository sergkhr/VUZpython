import math


def main(x):
    x = int(x, 16)
    r1 = x & 0b11
    r2 = x & 0b11111000
    r2 = r2 >> 2
    r1 = r1 << 6
    x = x & (~0b11111111)
    res = x | r1 | r2
    return res


a = '0x19e'
print(main(a))
