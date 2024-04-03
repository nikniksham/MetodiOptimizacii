from math import e, log
from sympy import *


def get_d(a, b):
    return ((a[0] - b[0])**2 + (a[1] - b[1])**2)**0.5


def method_gradient_descent(f_str, m_prev, step, eps):
    f = lambda x1, x2: eval(f_str)
    df_dx = lambda x1, x2: eval(str(diff(f_str, "x1")))
    df_dy = lambda x1, x2: eval(str(diff(f_str, "x2")))
    prev_delta = None
    print("Частная производная по x1 равна:", str(diff(f_str, "x1")))
    print("Частная производная по x2 равна:", str(diff(f_str, "x2")))
    it = 0
    while True:
        it += 1
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
        if delta <= eps:
            return m_next

        prev_delta = delta
        m_prev = m_next


def method_steepest_descent(f_str, m_prev, eps):
    f = lambda x1, x2: eval(f_str)
    df_dx = lambda x1, x2: eval(str(diff(f_str, "x1")))
    df_dy = lambda x1, x2: eval(str(diff(f_str, "x2")))
    prev_delta = None
    print(f_str)
    it = 0

    while True:
        it += 1
        print("Частная производная по x1 равна:", str(diff(f_str, "x1")))
        print("Частная производная по x2 равна:", str(diff(f_str, "x2")))
        print(f"Подставим точку m0 в производные: (x1, x2) = ({df_dx(*m_prev)}, {df_dy(*m_prev)})")

        print(f"{m_prev[0]} - h*{df_dx(*m_prev)}")
        print(f"{m_prev[1]} - h*{df_dy(*m_prev)}")

        expr_h = str(sympify(f_str).subs("x1", f"{m_prev[0]} - h*{df_dx(*m_prev)}").subs("x2", f"{m_prev[1]} - h*{df_dy(*m_prev)}"))
        print(expr_h)

        last_d, d = expr_h, expr_h
        while "h" in d:
            last_d = d
            d = str(diff(d, "h"))
        print(last_d)

        h = solve(sympify(last_d), "h")[0]
        # h = solve(sympify('536*h-166.75'), "h")[0]
        print(h)

        m_next = (m_prev[0] - h * df_dx(*m_prev), m_prev[1] - h * df_dy(*m_prev))
        print(f"{m_prev[0]} - {h}*{df_dx(*m_prev)} = {m_next[0]}")
        print(f"{m_prev[1]} - {h}*{df_dy(*m_prev)} = {m_next[1]}")

        m_prev = m_next
        input(f(*m_next))


if __name__ == '__main__':
    first = False
    second = True
    if first:
        # m0 = (0.7, 1)
        # step = 0.01
        m0 = (0, 0)
        step = 0.25
        eps = 0.05
        # f_str = "(x1**3 - 1)**4 + (x2 - x1)**2 - 2"
        f_str = "2*x1 + 4*x2 - x1**2 - 2*x2**2"
        # f_str = "e**(x1**2 + x2**2 + 2*x1*x2 + 2)"
        print(f"Вычисленная точка минимума функции {f_str} с заданным eps = {eps}: {method_gradient_descent(f_str, m0, step, eps)}")
    if second:
        f_str = "x1**2 + x2**2 + 1.5*x1*x2"
        m0 = (2, 3)
        eps = 0.05
        print(method_steepest_descent(f_str, m0, eps))

