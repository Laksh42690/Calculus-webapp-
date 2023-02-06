import numpy as np
from scipy.misc import derivative
from scipy.integrate import quad

def find_derivative(f, x):
    return derivative(f, x)

def find_integral(f, a, b):
    return quad(f, a, b)[0]

def find_minima(f, a, b, delta=0.01):
    x = np.arange(a, b, delta)
    y = f(x)
    min_idx = np.argmin(y)
    return x[min_idx], y[min_idx]

def find_maxima(f, a, b, delta=0.01):
    x = np.arange(a, b, delta)
    y = f(x)
    max_idx = np.argmax(y)
    return x[max_idx], y[max_idx]

def f(x):
    return x**2 + 3*x + 2

if __name__ == "__main__":
    x = 2
    print("Derivative at x =", x, ":", find_derivative(f, x))

    a, b = 0, 2
    print("Integral from", a, "to", b, ":", find_integral(f, a, b))

    print("Minimum value in the interval [", a, ",", b, "]:", find_minima(f, a, b))

    print("Maximum value in the interval [", a, ",", b, "]:", find_maxima(f, a, b))
