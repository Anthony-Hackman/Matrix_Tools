import sys, os
import sympy as sp

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Elementary_Matrix import to_rational_matrix

def test_elementary_row_operation():
    A_input = [
        [2, 4, -4],
        [8, -1, 3],
        [-3, 1, 5]
    ]

    E_input = [
        [1, 0, 0],
        [0, 1, 0],
        [0, -3, 1]
    ]

    A = to_rational_matrix(A_input)
    E = to_rational_matrix(E_input)
    EA = E * A

    expected = to_rational_matrix([
        [2, 4, -4],
        [8, -1, 3],
        [-27, 4, -4]  # fixed value
    ])

    assert EA.equals(expected), f"Expected EA to equal {expected}, but got {EA}"
