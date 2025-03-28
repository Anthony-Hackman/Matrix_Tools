import numpy as np

## REFERENCE ##
# Given system of equations:
# x1 + x2 - x3 = 1
# -3x1 - 2x2 + 2x3 = -5
# 2x1 + 2x2 - x3 = 0

# Coefficient matrix A
A = np.array([
    [1, 1, -1],
    [-3, -2, 2],
    [2, 2, -1]
])

# Right-hand side column (constants)
B = np.array([1, -5, 0])

# Compute determinant of A
det_A = np.linalg.det(A)

# Replace second column of A with B to compute det_A2
A2 = A.copy()
A2[:, 1] = B  # Replace second column with B
det_A2 = np.linalg.det(A2)

# Solve for x2 using Cramer's Rule
x2 = det_A2 / det_A

# Convert to integer if necessary
x2 = int(round(x2))

print(x2)
