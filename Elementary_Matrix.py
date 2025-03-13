"""
Anthony Hackman 3/13/2025
Elementary Matrix Script
Elementary matrix of an elementary row operation.
"""

import sympy as sp

def to_rational_matrix(matrix):
    """ Converts a given matrix with fractions into a SymPy Rational matrix """
    return sp.Matrix([[sp.Rational(str(val)) for val in row] for row in matrix])

# Define the elementary matrix E
""" PLACE QUOTES AROUND FRACTIONS """
"""
A_input = [
    [1, "-1/3", -3],
    ["-1/3", 10, 9],
    [2, -9, "-1/5"]
]
"""
E_input = [
    [1, 0, 0],
    [0, 1, 0],
    [0, -3, 1]
]

# Define matrix A
A_input = [
    [2, 4, -4],
    [8, -1, 3],
    [-3, 1, 5]
]

# Convert to SymPy matrices
E = to_rational_matrix(E_input)
A = to_rational_matrix(A_input)

# Compute EA
EA = E * A

# Display results
print("Elementary Matrix E:")
sp.pprint(E)

print("\nOriginal Matrix A:")
sp.pprint(A)

print("\nResult of EA:")
sp.pprint(EA)
