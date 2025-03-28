import sys, os
import sympy as sp

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from Matrix_Inversion import to_rational_matrix

def test_matrix_inversion_solution():
    A_input = [[-5, -7], [-2, -3]]
    b_input = [[-2], [-3]]

    A = to_rational_matrix(A_input)
    b = to_rational_matrix(b_input)
    A_inv = A.inv()
    x = A_inv * b

    expected = sp.Matrix([[-15], [11]])
    assert x == expected, f"Expected solution vector {expected} but got {x}"

