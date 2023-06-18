from math import sin, sqrt


def y(*args):
    if not args:
        return 'Отсутствуют введённые данные'
    try:
        x = float(args[0])
    except ValueError:
        return 'Введённые данные не являются числом'
    try:
        if x >= 0:
            return 1 + 2*sin(x**2)
        else:
            return sqrt(x**2 + 5)
    except ValueError:
        return 'Ошибка вычислений'
