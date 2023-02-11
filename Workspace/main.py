import math
import tkinter as tk


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

    c = 20
    x = (int(x * c) + 1) / c
    y = (int(y * c) + 1) / c
    res = x*63876 - y*572123
    res *= res * res * res
    n = math.cos(res) + math.sin(res)
    return n, n, n



label = tk.Label()
img = tk.PhotoImage(data=pyshader(func, 256, 256)).zoom(2, 2)
label.pack()
label.config(image=img)
tk.mainloop()
