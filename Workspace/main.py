import math
import tkinter as tk


c = 40 # number of cells in noise


def pyshader(func, w, h):
    scr = bytearray((0, 0, 0) * w * h)
    for y in range(h):
        for x in range(w):
            p = (w * y + x) * 3
            scr[p:p + 3] = [max(min(int(c * 255), 255), 0)
                            for c in func(x / w, y / h)]
    return bytes('P6\n%d %d\n255\n' % (w, h), 'ascii') + scr


# Ваш код здесь:
def func(x, y):
    # resgreeen = 0
    # resred = 0
    # rred = math.sqrt((x - 0.52) ** 2 + (y - 0.52) ** 2)
    # rgreen = math.sqrt((x - 0.48) ** 2 + (y - 0.48) ** 2)
    # resgreen = ((0.15 < rgreen < 0.3) * math.sin((rgreen - 0.3) * math.pi / -0.3)) or rgreen < 0.15
    # resred = ((0.15 < rred < 0.3) * math.sin((rred - 0.3) * math.pi / -0.3)) or rred < 0.15
    # return resred, resgreen, 0


    n = val_noise(x, y)
    return n, n, n


def smoothstep(edge1, edge2, x):
    t = max(min((x - edge1) / (edge2 - edge1), 1.0), 0.0)
    return t * t * (3.0 - 2.0 * t)


def noise(x, y):
    x = (int(x * c) + 1) / c
    y = (int(y * c) + 1) / c
    res = x * 63876 - y * 572123
    res *= res * res * res
    n = math.cos(res) + math.sin(res)
    return n


def val_noise(x, y):
    #use linear interpolation
    x0 = int(x * c)
    x1 = (x0 + 1)
    y0 = int(y * c)
    y1 = (y0 + 1)
    x0 /= c
    x1 /= c
    y0 /= c
    y1 /= c
    smoothX = smoothstep(x0, x1, x)
    smoothY = smoothstep(y0, y1, y)
    n = (smoothX) * (smoothY)
    return n




label = tk.Label()
img = tk.PhotoImage(data=pyshader(func, 256, 256)).zoom(2, 2)
label.pack()
label.config(image=img)
tk.mainloop()
