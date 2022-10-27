# Exercise 2

import numpy as np

e = np.exp(1)

a = lambda n: (1 + 1/n)**n

for n in range(1000, 100000, 1000):
    print(np.abs(a(n) - e))

# We can see that the error between the series and the real number
# gets smaller and smaller as n grows.