import sys
import os
import numpy as np

# Make sure the toolkit can be imported from the parent directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Linear_Algebra_Toolkit import get_cofactor

def test_known_cofactor():
    """
    Test the cofactor of a known 3x3 matrix.
    Matrix:
        A = [[2, -3, 1],
             [2, 0, -1],
             [1, 4, 5]]

    The cofactor of A[0][0] should be:
    Cofactor = (-1)^(0+0) * det([[0, -1], [4, 5]]) = 1 * ((0*5) - (-1*4)) = 4
    """
    A = np.array([
        [2, -3, 1],
        [2, 0, -1],
        [1, 4, 5]
    ])

    expected = 4
    result = round(get_cofactor(A, 0, 0))
    assert result == expected, f"Expected cofactor 4 but got {result}"
