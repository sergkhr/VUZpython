import math


def main(n, a, b, p):
    temp = 0
    for c in range(1, a+1):
        for j in range(1, n+1):
            temp += 67 - math.log2(c)**4/69 - math.cos(j)
    for k in range(1, n+1):
        for i in range(1, b+1):
            temp += math.log(i) - 58*(1 - 90*p**2 - 39*i)**6 - math.sqrt(k)**5
    return temp


n = int(input("Enter n: "))
a = int(input("Enter a: "))
b = int(input("Enter b: "))
p = float(input("Enter p: "))
print(main(n, a, b, p))
