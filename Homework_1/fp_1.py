# Author Davide Gardenal

# Floating Point Arithmetic
# Exercise 1

eps = 1.1102264604090055e-16
it = 1

print("Epsilon after:")
while 1 + eps > 1:
    if it % 1e6 == 0: print(f"{it} iterations \t-> {eps}")
    eps = eps / (eps + 1)
    it += 1

# eps = 1.1102264604090055e-16 with eps = eps / 1.0001