import math


def main(y, z, x):
    n = len(y)
    temp = 0
    for i in range(1, n+1):
        temp += 96*z[n + 1 - math.ceil(i/2) - 1]**3 \
                - 14*x[n + 1 - i - 1]**2 - y[i - 1]
    return temp


y = [-0.62, 0.69, 0.63, -0.09]
z = [0.49, 0.04, 0.55, 0.17]
x = [-0.92, 0.99, 0.83, -0.87]
print(main(y, z, x))
