import random


def fast_mul(a, b):
    result = 0
    while b:
        if b & 1:
            result += a
        a <<= 1
        b >>= 1
    return result


def fast_pow(a, b):
    result = 1
    while b:
        if b & 1:
            result = fast_mul(result, a)
        a = fast_mul(a, a)
        b >>= 1
    return result


for i in range(10):
    a = random.randint(0, 1000)
    b = random.randint(0, 1000)
    assert fast_mul(a, b) == a * b
print("OK")

for i in range(10):
    a = random.randint(0, 1000)
    b = random.randint(0, 1000)
    assert fast_pow(a, b) == a ** b
print("OK")


def mul_bits(x, y, bits):
    x &= (2 ** bits - 1)
    y &= (2 ** bits - 1)
    return x * y


def mul16(x, y):
    xa = x >> 8
    xb = x & 255
    ya = y >> 8
    yb = y & 255

    p1 = mul_bits(xa, ya, 8)
    p2 = mul_bits(xa, yb, 8)
    p3 = mul_bits(xb, ya, 8)
    p4 = mul_bits(xb, yb, 8)

    # (a1*256 + b1) * (a2*256 + b2) = a1*a2*256*256 + a1*b2*256 + b1*a2*256 + b1*b2
    return (p1 << 16) + ((p2 + p3) << 8) + p4

for i in range(10):
    a = random.randint(0, 1000)
    b = random.randint(0, 1000)
    assert mul16(a, b) == a * b
print("OK")
