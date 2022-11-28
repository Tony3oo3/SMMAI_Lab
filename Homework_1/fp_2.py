# Author Davide Gardenal

# Floating Point Arithmetic
# Exercise 2

import numpy as np

e = np.exp(1)
a = lambda n: (1 + 1/n)**n

print("Absolute error for:")
for n in range(1000, 100000, 1000):
    print(f"n = {n} \t-> {np.abs(a(n) - e)}")
