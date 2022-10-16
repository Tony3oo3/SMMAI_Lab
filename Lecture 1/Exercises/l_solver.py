# Exercise: Write a function that takes as input a non-singular matrix A∈Rn×n 
# and a vector y∈Rn and returns the solution x∈Rn of Ax=y without using np.linalg.lu.

import numpy as np
import scipy

n = 10

A = np.random.randn(n, n) # non singular matrix
y = np.random.randn(n) # solution vector

A_inv = np.linalg.inv(A)
print(y @ A_inv)

def solve(A, y):
    # LU factorization of A
    P, L, U = scipy.linalg.lu(A)

    # Solve Lz = Py
    z = np.linalg.solve_triangular(L, P@y)

    # Solve Ux = z
    x = np.linalg.solve_triangular(U, z)

    return x

print(solve(A, y))