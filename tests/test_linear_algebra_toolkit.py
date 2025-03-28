import sys
import os
import numpy as np

# Ensure the parent directory (repo root) is in the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Linear_Algebra_Toolkit import determinant, inverse_exists

def test_determinant_identity():
    """The determinant of an identity matrix should be 1."""
    identity = np.identity(3)
    assert round(determinant(identity)) == 1

def test_determinant_known_matrix():
    """Test a known 2x2 matrix determinant."""
    matrix = np.array([[4, 6], [3, 8]])
    assert round(determinant(matrix)) == 14

def test_inverse_exists_identity():
    """Identity matrix should always be invertible."""
    identity = np.identity(4)
    assert inverse_exists(identity) is True

def test_inverse_exists_singular():
    """Matrix with a row of zeros should not be invertible."""
    singular = np.array([[1, 2], [0, 0]])
    assert inverse_exists(singular) is False
