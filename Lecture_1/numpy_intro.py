import numpy as np

# Create array
a = [3, 1, 4]
a_np = np.array(a)

# Check the shape
print(a_np.shape)

# Create matrices
A = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
print(A.shape)

# Create a vector of len n and with x[0] = a, x[n-1] = b
a = 0
b = 1
n = 50
x = np.linspace(a, b, n)
print(x)

# Create a matrix filled with zeros
x = np.zeros((3,2))
print(x)

# Create a matrix filled with ones
x = np.ones((3,2))
print(x)

# Create a matrix filled with random value (normal distribution)
A = np.random.randn(3, 2)
print(A)

# Operations
x = np.ones((3, ))
y = np.ones((3, ))
print(x + y) # + - * / **

# Scalar operations
print(3 * x)

# Row by col mult
A = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
x = 2 * np.ones((3, ))
print(A @ x)

# Element wise function application
x = np.linspace(0, 1, 20)
y = np.sin(x) # sin, cos, tan, ecc.
print(y.shape)

# Logic operations
a = np.array([1, 2, 3])
b = np.array([3, 2, 1])
print(a == b) # Element wise comparison
print(a >= 2) # Vector with scalar comparison

# Indexed access
A = np.array([[1, 2, 3],[4, 5, 6]])
x = np.array([1, 2, 3])
print(x)
print(x[1])
print(A)
print(A[1, 1])

# Slicing
print(x[1:])
print(x[:2])
print(A[:, :2])

# Slicing with booleans arrays
A = np.random.randn(3, 3)
print(A)
print(A[A > 0]) # A > 0 is a matrix of bool

# Matrix manipulation
A = np.array([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
print(A)
    # Transpose
print(A.T)
    # Rank
print(np.linalg.matrix_rank(A))
    # Inverse
print(np.linalg.inv(A)) # Very slow
    # Condition number
p = 2
# p = 'fro'
# p = np.Inf
print(np.linalg.cond(A, p))
    # Norm
print(np.linalg.norm(A, p)) # Can be used with vectors
    # Reshaping
A = np.random.randn(8, 2)
print(A)
print(np.reshape(A, (4, 4))) # Reshaped by rows by default.