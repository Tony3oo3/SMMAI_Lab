# Author: Davide Gardenal

# Direct Methods for the solution of Linear System
# Exercise 1 and 2

import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg

def es1(A):
    x_true = np.ones((A.shape[0], ))

    # 1.1
    b = A @ x_true
    # print(f"b = ")
    # print(b)

    # 1.2
    condn_n2 = np.linalg.cond(A, 2)
    condn_ninf = np.linalg.cond(A, np.inf)
    print("Condition number with:")
    print(f"2-norm \t\t-> {condn_n2}")
    print(f"inf-norm \t-> {condn_ninf}")

    # 1.3
    x = np.linalg.solve(A, b)
    print("x = ", x)

    # 1.4
    error = np.linalg.norm(x - x_true, 2) / np.linalg.norm(x_true, 2)
    print(f"Rel. error \t-> {error}")
    print()

    return error, condn_n2, condn_ninf

def plot_error(x, y, title=""):
    plt.plot(x, y)
    plt.title(title)
    plt.xlabel("n")
    plt.ylabel("relative error")
    plt.show()
    return

def plot_condn(x, y1, y2, title=""):
    plt.plot(x, y1)
    plt.plot(x, y2)
    plt.title(title)
    plt.xlabel("n")
    plt.ylabel("conditional number")
    plt.legend(["2-norm", "inf-norm"])
    plt.show()
    return

def generate_points(matrix_generator, range):
    x = []
    y_error = []
    y_condn2 = []
    y_condnInf = []
    for n in range:
        print(f"n = {n}")
        A = matrix_generator(n)
        error, cn2, cnInf = es1(A)

        x.append(n)
        y_error.append(error)
        y_condn2.append(cn2)
        y_condnInf.append(cnInf)
    
    return x, y_error, y_condn2, y_condnInf

# Random matrix
print("==> Random Matrix")
x, y_error, y_c2, y_cI = generate_points(lambda n: np.random.rand(n, n), range(10, 101, 10))
plot_error(x, y_error, title="Random")
plot_condn(x, y_c2, y_cI, title="Random")

# Vandermonde matrix
print("==> Vandermonde Matrix")
x, y_error, y_c2, y_cI = generate_points(lambda n: np.vander(np.linspace(0, n, n)), range(5, 31, 5))
plot_error(x, y_error, title="Vandermonde")
plot_condn(x, y_c2, y_cI, title="Vandermonde")

# Hilbert matrix
print("==> Hilbert Matrix")
x, y_error, y_c2, y_cI = generate_points(lambda n: scipy.linalg.hilbert(n), range(4, 13))
plot_error(x, y_error, title="Hilbert")
plot_condn(x, y_c2, y_cI, title="Hilbert")
