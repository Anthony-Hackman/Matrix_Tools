import numpy as np

## REFERENCE ##
# Given system of equations:
# x1 - 2x2 = 13
# 3x1 - 5x2 = 35

# Coefficient matrix A
A = np.array([[1, -2],
              [3, -5]])

# Right-hand side column (constants)
B = np.array([13, 35])

# Compute determinants using Cramer's Rule
det_A = np.linalg.det(A)

# Replace first column of A with B to compute det_A1
A1 = A.copy()
A1[:, 0] = B  # Replace first column with B
det_A1 = np.linalg.det(A1)

# Replace second column of A with B to compute det_A2
A2 = A.copy()
A2[:, 1] = B  # Replace second column with B
det_A2 = np.linalg.det(A2)

# Solve for x1 and x2
x1 = det_A1 / det_A
x2 = det_A2 / det_A

# Convert to integers if needed (since solutions are typically exact)
x1, x2 = int(round(x1)), int(round(x2))

print(x1, x2)
