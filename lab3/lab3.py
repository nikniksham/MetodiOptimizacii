from math import e, log
from sympy import *


def get_d(a, b):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5


def method_gradient_descent(f_str, m_prev, step, eps):
    f = lambda x1, x2: eval(f_str)
    df_dx = lambda x1, x2: eval(str(diff(f_str, "x1")))
    df_dy = lambda x1, x2: eval(str(diff(f_str, "x2")))
    prev_delta, delta = None, None
    print("Частная производная по x1 равна:", str(diff(f_str, "x1")))
    print("Частная производная по x2 равна:", str(diff(f_str, "x2")))
    it = 0
    while True:
        if delta is not None and delta <= eps:
            print(m_prev, f(*m_prev))
            print(f"Вычисленная точка минимума функции: {m_prev}, значение функции: {f(*m_prev)}")
            return m_prev

        it += 1
        print(f"Итерация {it}")
        m_next = (m_prev[0] + step * df_dx(*m_prev), m_prev[1] + step * df_dy(*m_prev))
        print(f"x1({it}) = {m_prev[0]} + {step} * {df_dx(*m_prev)} = {m_next[0]}")
        print(f"x2({it}) = {m_prev[1]} + {step} * {df_dy(*m_prev)} = {m_next[1]}")
        delta = abs(f(*m_next) - f(*m_prev))
        print(f"Вычислим значение функции цели в новой точке и определим степень приближения:"
              f" |f(x({it})) - f(x({it-1}))| = |{f(*m_next)} - {f(*m_prev)}| =  {delta}")
        if prev_delta is not None and delta > prev_delta:
            step /= 2
            print(f"Функция начала увеличиваться => шаг слишком большой. Уменьшаем шаг в 2 раза step = {step}")
            continue

        prev_delta = delta
        # print(f(*m_prev), f(*m_next))
        m_prev = m_next
        print("\n-------------------------------------------------------------\n")


def method_steepest_descent(f_str, m_prev, eps, logs=False):
    f = lambda x1, x2: eval(f_str)
    df_dx1 = lambda x1, x2: eval(str(diff(f_str, "x1")))
    df_dx2 = lambda x1, x2: eval(str(diff(f_str, "x2")))
    prev_delta = None
    print(f_str)
    it = 0

    while True:
        # print((df_dx1(*m_prev)**2 + df_dx2(*m_prev)**2)**0.5)
        if ((df_dx1(*m_prev)**2 + df_dx2(*m_prev)**2)**0.5) <= eps:
            return m_prev
        it += 1
        print(f"Итерация {it}")

        eq_x1 = f"{m_prev[0]} - h*{df_dx1(*m_prev)}"
        eq_x2 = f"{m_prev[1]} - h*{df_dx2(*m_prev)}"
        if logs:
            print("Частная производная по x1 равна:", str(diff(f_str, "x1")))
            print("Частная производная по x2 равна:", str(diff(f_str, "x2")))
            print(f"Подставим точку m0 в производные: (x1, x2) = ({df_dx1(*m_prev)}, {df_dx2(*m_prev)})")

            print(f"На что будем менять x1: {eq_x1}")
            print(f"На что будем менять x2: {eq_x2}")

        expr_h = str(sympify(f_str).subs("x1", eq_x1).subs("x2", eq_x2))
        if logs:
            print(expr_h)

        d = str(diff(expr_h, "h"))
        if logs:
            print(f"Уравнение, из которого выражаем h: {d}")

        h = solve(sympify(d), "h")[0]
        # h = solve(sympify('536*h-166.75'), "h")[0]
        if logs:
            print(f"h = {h}")

        m_next = (m_prev[0] - h * df_dx1(*m_prev), m_prev[1] - h * df_dx2(*m_prev))
        if logs:
            print(f"x1({it}) = {m_prev[0]} - {h} * {df_dx1(*m_prev)} = {m_next[0]}")
            print(f"x2({it}) = {m_prev[1]} - {h} * {df_dx2(*m_prev)} = {m_next[1]}")

        m_prev = m_next
        # if logs:
        print(f"Вычисленная точка m{it} = {m_prev}, значение функции в ней: {f(*m_prev)}")
        print("\n-------------------------------------------------------------\n")


if __name__ == '__main__':
    first = False
    second = True
    if first:
        m0 = (-0.7, -1)
        step = -0.01
        # m0 = (0, 0)
        # step = 0.25
        # f_str = "(x1**3 - 1)**4 + (x2 - x1)**2 - 2"
        # f_str = "x1**4 + x2**4 - 4*x1*x2"
        f_str = "4*x1**2 + 3*x2**2 + 16*x1 - 4*x2"
        eps = 0.005
        method_gradient_descent(f_str, m0, step, eps)
    if second:
        print("\n\n=======================================")
        print("=======================================")
        print("=======================================\n\n")
        f_str = "x1**2 + x2**2 + 1.5*x1*x2"
        # f_str = "(x1**3 - 1)**4 + (x2 - x1)**2 - 2"
        # f_str = "4 * x1 ** 2 + 3 * x2 ** 2 + 16 * x1 - 4 * x2"
        # f_str = "x1**4 + x2**4 - 4*x1*x2"
        # f_str = "4*x1**2 + 3*x2**2 + 16*x1 - 4*x2"

        m0 = (0, 1)
        # m0 = (-0.7, -1)
        eps = 0.05
        method_steepest_descent(f_str, m0, eps, True)

