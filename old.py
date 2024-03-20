from math import log, sin, e, pi

k = 0.0001
delta_x = 1


def f(x):
    return log(x**2 + 1, e) - sin(x)


def quadratic_approximation_method(x1, x2=None, x3=None):
    f1 = f(x1)
    if x2 is None:
        x2 = x1 + delta_x
        f2 = f(x2)
        if f1 > f2:
            x3 = x1 + delta_x * 2
        else:
            x3 = x1 - delta_x
        f3 = f(x3)
    else:
        f2, f3 = f(x2), f(x3)
    fmin, xmin = min(f1, f2, f3), x1
    if fmin == f2:
        xmin = x2
    elif fmin == f3:
        xmin = x3

    if (x2 - x3)*f1 + (x3 - x1)*f2 + (x1 - x2)*f3 == 0:
        print(1)
        return quadratic_approximation_method(xmin)
    chert = 1/2 * ((x2**2 - x3**2)*f1 + (x3**2 - x1**2)*f2 + (x1**2 - x2**2)*f3)/((x2 - x3)*f1 + (x3 - x1)*f2 + (x1 - x2)*f3)
    fchert = f(chert)

    cond_1, cond_2 = abs((fmin - fchert) / fchert) < k, abs((xmin - chert) / chert) > k
    if cond_1 and cond_2:
        return chert
    elif cond_1 or cond_2:
        if x1 <= chert <= x3 or x1 >= chert >= x3:
            return quadratic_approximation_method(x1, chert, x3)
        return quadratic_approximation_method(chert)


res = quadratic_approximation_method(pi/8)
print(res, f(res))
# x1, x2, x3 = 0, pi/8, pi/4
# f1, f2, f3 = f(x1), f(x2), f(x3)
# print(f"f1 = f({x1}) = {f1}")
# print(f"f2 = f({x2}) = {f2}")
# print(f"f3 = f({x3}) = {f3}")
# fmin = min(f1, f2, f3)
# print(f"fmin = {fmin}")
# xmin = 1/2 * ((x2**2 - x3**2)*f1 + (x3**2 - x1**2)*f2 + (x1**2 - x2**2)*f3)/((x2 - x3)*f1 + (x3 - x1)*f2 + (x1 - x2)*f3)
# fxmin = f(xmin)
# print(f"xmin = {xmin}, f(xmin) = {fxmin}")