# Matrix_Tools ![License](https://img.shields.io/github/license/Anthony-Hackman/Matrix_Tools) https://img.shields.io/badge/python-3.9%20|%203.10%20|%203.11-blue
[![Python package](https://github.com/Anthony-Hackman/Matrix_Tools/actions/workflows/python-package.yml/badge.svg?branch=main)](https://github.com/Anthony-Hackman/Matrix_Tools/actions/workflows/python-package.yml)


**Matrix_Tools** is a collection of Python scripts designed to perform foundational matrix operations with applications in linear algebra, numerical methods, and algorithmic problem-solving. This repository demonstrates both numerical and symbolic computation by leveraging the power of `numpy` and `sympy`.

## Key Features

- **Determinant Calculations:** Quickly compute determinants of square matrices.
- **Matrix Inversion & Linear Systems:** Solve systems using matrix inversion.
- **LU Decomposition:** Decompose matrices and compute inverses using L⁻¹·U⁻¹.
- **Elementary Matrices:** Perform and visualize row operations.
- **Dot Products & Vector Angles:** Calculate dot products and determine angles between vectors.
- **Cramer’s Rule:** Solve 2x2 and 3x3 linear systems using Cramer’s Rule.

## Contents

| File                        | Description                                                                    |
|-----------------------------|--------------------------------------------------------------------------------|
| `linear_algebra_toolkit.py` | Main() Interactive CLI tool for computing determinants, inverses, cofactors, etc.|
| `Matrix_Inversion.py`       | Solves linear systems using the matrix inversion method.                       |
| `LU_Decomposition.py`       | Performs LU decomposition and computes the inverse via L⁻¹·U⁻¹.                 |
| `Elementary_Matrix.py`      | Demonstrates row operations using elementary matrices.                         |
| `Cramers_2x2.py`            | Solves a 2x2 system using Cramer’s Rule.                                         |
| `Cramers_3x3.py`            | Solves a 3x3 system using Cramer’s Rule.                                         |
| `DotAngle.py`               | Computes the angle between two vectors using the dot product.                  |

## Requirements

- Python 3.7 or higher
- [`numpy`](https://numpy.org/)
- [`sympy`](https://www.sympy.org/)

Install the required packages with:

```bash
pip install numpy sympy
```

## Usage

Clone the repository:

```bash
git clone https://github.com/Anthony-Hackman/Matrix_Tools.git
cd Matrix_Tools
```

Run the interactive CLI tool:

```bash
python linear_algebra_toolkit.py
```

Alternatively, you can execute any standalone script included. For example:

```bash
python Matrix_Inversion.py
```

## Purpose

This repository was created to serve as both an educational tool and a practical resource for experimenting with linear algebra operations. It is intended to support:

- **Students** learning about matrix computations and linear algebra.
- **Developers** experimenting with matrix-based algorithms.
- **Enthusiasts** exploring both numerical and symbolic matrix manipulations.

## Contributing

Contributions are welcome! If you have ideas for improvements, bug fixes, or new features, please feel free to open an issue or submit a request.

## License

This project is licensed under the MIT License. See the [`LICENSE`](LICENSE) file for details.

## Author

Anthony Hackman  
March 2025
