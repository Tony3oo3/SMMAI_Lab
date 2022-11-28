# Author Davide Gardenal

# Floating Point Arithmetic
# Exercise 3

import numpy as np

A = np.array([[4, 2], [1, 3]])
B = np.array([[4, 2], [2, 1]])

# Compute the rank of A and B
A_rank = np.linalg.matrix_rank(A)
B_rank = np.linalg.matrix_rank(B)

print(f"A rank = {A_rank}")
print(f"B rank = {B_rank}")

## Compute the eigenvalues of A and B
A_eigvals = np.linalg.eigvals(A)
B_eigvals = np.linalg.eigvals(B)

print(f"A eigenvalues are = {A_eigvals}")
print(f"B eigenvalues are = {B_eigvals}")
