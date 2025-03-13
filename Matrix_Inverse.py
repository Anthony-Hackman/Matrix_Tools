"""
Anthony Hackman 3/13/2025
Matrix Inversion Script
Using an inverse matrix to solve a system of equations
"""
import sympy as sp

def to_rational_matrix(matrix):
    """ Converts a given matrix with fractions into a SymPy Rational matrix """
    return sp.Matrix([[sp.Rational(str(val)) for val in row] for row in matrix])

# Define the coefficient matrix using standard fraction notation
""" PLACE QUOTES AROUND FRACTIONS """
"""
A_input = [
    [1, "-1/3", -3],
    ["-1/3", 10, 9],
    [2, -9, "-1/5"]
]
"""
# Define the coefficient matrix
A_input = [
    [-5, -7],
    [-2, -3]
]

# Define the column vector b
b_input = [
    [-2],
    [-3]
]

# Convert to a SymPy Rational matrix
A = to_rational_matrix(A_input)
b = to_rational_matrix(b_input)

# Compute the inverse
A_inv = A.inv()

# Solve for x using matrix multiplication
x = A_inv * b

# Display results
print("Original Matrix A:")
sp.pprint(A)

print("\nInverse Matrix A⁻¹:")
sp.pprint(A_inv)

print("\nSolution Vector x:")
sp.pprint(x)
