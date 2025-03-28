"""
Anthony Hackman 3/13/2025
LU Decomposition Script
"""

import sympy as sp

def to_rational_matrix(matrix):
    """ Converts a given matrix with fractions into a SymPy Rational matrix """
    return sp.Matrix([[sp.Rational(str(val)) for val in row] for row in matrix])

# Define the coefficient matrix A
A_input = [
    [1, 3, -1],
    [-4, -11, 1],
    [5, 10, 11]
]

# Convert to SymPy Matrix
A = to_rational_matrix(A_input)

# Perform LU decomposition
L, U, _ = A.LUdecomposition()

# Compute Inverses of L and U
L_inv = L.inv() if L.det() != 0 else "Matrix L is singular (not invertible)"
U_inv = U.inv() if U.det() != 0 else "Matrix U is singular (not invertible)"

# Compute Inverse of A using A⁻¹ = U⁻¹ * L⁻¹
if isinstance(L_inv, str) or isinstance(U_inv, str):  # If L or U is singular
    A_inv = "Matrix A is singular (not invertible)"
else:
    A_inv = U_inv * L_inv

# Display results
print("Lower Triangular Matrix L:")
sp.pprint(L)

print("\nInverse of L (L⁻¹):")
sp.pprint(L_inv)

print("\nUpper Triangular Matrix U:")
sp.pprint(U)

print("\nInverse of U (U⁻¹):")
sp.pprint(U_inv)

print("\nInverse of A (A⁻¹ = U⁻¹ * L⁻¹):")
sp.pprint(A_inv)
