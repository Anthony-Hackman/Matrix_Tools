"""
Anthony Hackman - 3/13/2025
Matrix Inversion Script
Solves a system of equations using the inverse matrix method.
"""

import sympy as sp

def to_rational_matrix(matrix):
    """Convert a matrix with fractions/decimals to SymPy Rational form."""
    return sp.Matrix([[sp.Rational(str(val)) for val in row] for row in matrix])

def main():
    # Define the coefficient matrix A and right-hand side vector b
    A_input = [
        [-5, -7],
        [-2, -3]
    ]
    b_input = [
        [-2],
        [-3]
    ]

    A = to_rational_matrix(A_input)
    b = to_rational_matrix(b_input)

    # Compute the inverse of A
    A_inv = A.inv()

    # Solve for x using A⁻¹ * b
    x = A_inv * b

    # Display results
    print("Original Matrix A:")
    sp.pprint(A)

    print("\nInverse Matrix A⁻¹:")
    sp.pprint(A_inv)

    print("\nSolution Vector x:")
    sp.pprint(x)
