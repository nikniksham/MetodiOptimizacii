x, y, h = symbols('x y h')


def f(x, y):
    return x ** 2 + y ** 2 + 2 * x - y


def gradient1(x_, y_):
    return [2 * x_ + 2, 2 * y_ - 1]


def gradient_module1(x_1, y_1):
    dx, dy = gradient1(x_1, y_1)
    return sqrt(dx ** 2 + dy ** 2).evalf()


def steepest_descent_method(x_0, y_0, eps):
    iteration_count = 0
    d = gradient_module1(x_0, y_0)
    while (d.evalf() > eps):
        grad_x, grad_y = gradient1(x_0, y_0)
        x_new = x_0 - h * grad_x
        y_new = y_0 - h * grad_y
        f_new = f(x_new, y_new)
        df_new_h = diff(f_new, h)
        h_solution = solve(df_new_h, h)
        d = gradient_module1(x_0, y_0)
        if h_solution:
            h_new = h_solution[0].evalf()
            x_0 -= h_new * grad_x
            y_0 -= h_new * grad_y
            iteration_count += 1
        else:
            print("Решение для h не найдено.")
            break
    print("x = " + str(x_0) + " y = " + str(y_0) + " Количество итераций " + str(iteration_count))


steepest_descent_method(0, 0, 0.0001)
