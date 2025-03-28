import sys, os
import sympy as sp

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from LU_Decomposition import to_rational_matrix

def test_lu_reconstruction():
    A_input = [
        [1, 3, -1],
        [-4, -11, 1],
        [5, 10, 11]
    ]
    A = to_rational_matrix(A_input)
    L, U, _ = A.LUdecomposition()

    # A should equal L * U
    reconstructed = L * U
    assert reconstructed.equals(A), f"L*U did not reconstruct A correctly"
