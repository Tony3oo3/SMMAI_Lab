eps = 1.1102264604090055e-16
it = 1

while 1 + eps > 1:
    if it % 1e6 == 0: print(eps)
    eps = eps / (eps + 1)
    it += 1

# eps = 1.1102264604090055e-16 with eps = eps / 1.0001

# Explanation
# Start with a small epsilon that was computed with eps = eps / 1.0001 inside the while loop
# TODO