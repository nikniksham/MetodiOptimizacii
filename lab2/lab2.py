from math import log, sin, e, pi

k = 0.0001
delta_x = 1


def f(x):
    return log(x**2 + 1, e) - sin(x)


def quadratic_approximation_method(x1):
    x2 = x1 + delta_x
    if f(x1) > f(x2):
        x3 = x1 + delta_x * 2
    else:
        x1, x2, x3 = x1 - delta_x, x1, x2
    f1, f2, f3 = f(x1), f(x2), f(x3)

    while True:
        fmin, xmin = min(f1, f2, f3), x1
        if fmin == f2:
            xmin = x2
        elif fmin == f3:
            xmin = x3

        znam = (x2 - x3) * f1 + (x3 - x1) * f2 + (x1 - x2) * f3
        if znam == 0:
            return quadratic_approximation_method(xmin)

        chert = 1/2 * ((x2**2 - x3**2)*f1 + (x3**2 - x1**2)*f2 + (x1**2 - x2**2)*f3)/znam
        fchert = f(chert)
        print(f"f1 = f({x1}) = {f1}")
        print(f"f2 = f({x2}) = {f2}")
        print(f"f3 = f({x3}) = {f3}")
        print(f"chert = {chert}, f({chert}) = {fchert}")
        print(f"разность = {abs((fmin - fchert) / fchert)}")
        print()
        if abs((fmin - fchert) / fchert) < k:
            return chert

        if x1 <= chert <= x3:
            if chert < x2:
                x3, f3 = x2, f2
            else:
                x1, f1 = x2, f2
            x2, f2 = chert, fchert
        else:
            print(123)
            return quadratic_approximation_method(chert)


res = quadratic_approximation_method(0)
print(res, f(res))
