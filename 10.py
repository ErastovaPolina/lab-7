import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 2 ** x + 5 * x - 3

def g(x):
    return (3 - 2 ** x) / 5

def simple_iteration_method(g, x0, eps=1e-6, max_iter=1000):
    iter_count = 0
    x_prev = x0
    x_next = g(x_prev)
    while abs(x_next - x_prev) >= eps and iter_count < max_iter:
        x_prev = x_next
        x_next = g(x_prev)
        iter_count += 1
    return x_next, iter_count

def draw_graphic(a, b):
    window = plt.figure()
    axes = window.add_subplot()
    axes.set_title('График функции')
    axes.set_xlabel('Ox')
    axes.set_ylabel('Oy')
    axes.grid()
    axes.axvline()
    axes.axhline()
    x = np.linspace(a, b, 100)
    y = f(x)
    axes.plot(x, y, label='f(x) = 2^x + 5x - 3', color='r')
    plt.show()

def main():
    x0 = 0.5
    root, iterations = simple_iteration_method(g, x0)

    a = float(input('Введите a: '))
    b = float(input('Введите b: '))

    draw_graphic(a, b)

    print("Корень уравнения: ", root)
    print("Количество итераций: ", iterations)

if __name__ == "__main__":
    main()
