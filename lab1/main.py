from math import log, sin, e, pi, cos


def f(x):
    return log(1 + x**2, e) - sin(x)


def d(x):
    return 2*x/(x**2 + 1) - cos(x)


def d2(x):
    return sin(x) - (2*x**2 - 2) / (x**4 + 2*x**2 + 1)


def method_polovinnogo_deleniya(a, b, k):
    while (b-a) > k * 2:
        x1, x2 = (a + b - k)/2, (a + b + k)/2
        y1, y2 = f(x1), f(x2)
        if y1 > y2:
            a = x1
        else:
            b = x2
    return (b+a)/2


def method_zolotogo_secheniya(a, b, k):
    x1, x2 = b - (b-a)/1.618, a + (b-a)/1.618
    y1, y2 = f(x1), f(x2)
    while (b-a) > k:
        print(a, x1, x2, b)
        if y1 > y2:
            a, x1, y1 = x1, x2, y2
            x2 = a + (b-a)/1.618
            y2 = f(x2)
        else:
            b, x2, y2 = x2, x1, y1
            x1 = b - (b-a)/1.618
            y1 = f(x1)
    return (b+a)/2


def method_hord(a, b, k):
    while True:
        x = a - d(a) / (d(b) - d(a)) * (b - a)
        dx = d(x)
        if dx > 0:
            b = x
        else:
            a = x
        if abs(dx) <= k:
            return x


def method_newton(a, b, k):
    x = (a + b) / 2
    while abs(d(x)) > k:
        x = x - d(x) / d2(x)
    return x


k = 0.001
a = 0
b = pi/4

znach1 = method_polovinnogo_deleniya(a, b, k)
print(f"Метод половинного деления:\nf({znach1}) = {f(znach1)}")
znach2 = method_zolotogo_secheniya(a, b, k)
print(f"Метод золотого сечения:\nf({znach2}) = {f(znach2)}")
znach3 = method_hord(a, b, k)
print(f"Метод хорд:\nf({znach3}) = {f(znach3)}")
znach4 = method_newton(a, b, k)
print(f"Метод Ньютона:\nf({znach4}) = {f(znach4)}")
