import numpy as np

def get_matrix():
    """
    Prompts the user to input a square matrix row by row.

    Allows undoing the last row or restarting the entire matrix input.

    @return: numpy.ndarray - a square matrix entered by the user
    @raises: ValueError - if the matrix is not square or input is invalid
    """
    print("Enter your square matrix row by row (e.g. 1 2 3). Type 'done' when finished:")
    print("Type 'undo' to remove the last row or 'restart' to start over.")
    rows = []
    while True:
        print(f"\nCurrent matrix ({len(rows)} rows):")
        for r in rows:
            print("  ", r)

        row = input(f"Row {len(rows)+1}: ").strip()

        if row.lower() == 'done':
            break
        elif row.lower() == 'undo':
            if rows:
                removed = rows.pop()
                print(f"Removed row: {removed}")
            else:
                print("No rows to undo.")
            continue
        elif row.lower() == 'restart':
            rows = []
            print("Matrix cleared. Start again.")
            continue

        try:
            row_vals = list(map(float, row.split()))
            if rows and len(row_vals) != len(rows[0]):
                print("All rows must have the same number of elements.")
                continue
            rows.append(row_vals)
        except ValueError:
            print("Please enter valid numbers separated by spaces.")

    matrix = np.array(rows)
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Matrix must be square.")
    return matrix

def determinant(matrix):
    return np.linalg.det(matrix)

def inverse_exists(matrix):
    return not np.isclose(np.linalg.det(matrix), 0)

def get_inverse(matrix):
    """
    Computes the inverse of a matrix.

    @param matrix: numpy.ndarray - input square matrix
    @return: numpy.ndarray - inverse of the matrix if it exists
    @raises: LinAlgError - if the matrix is singular
    """
    return np.linalg.inv(matrix)

def get_minor(matrix, row, col):
    sub = np.delete(np.delete(matrix, row, axis=0), col, axis=1)
    return np.linalg.det(sub)

def get_cofactor(matrix, row, col):
    minor = get_minor(matrix, row, col)
    return ((-1) ** (row + col)) * minor

def check_collinearity(matrix):
    det = np.linalg.det(matrix)
    return np.isclose(det, 0)

def main():
    print("\n===== Linear Algebra Toolkit =====\n")
    try:
        A = get_matrix()
    except ValueError as e:
        print(f"Error: {e}")
        return

    while True:
        print("\nChoose an operation:")
        print("1. Compute Determinant")
        print("2. Check Invertibility & Show Inverse")
        print("3. Check Collinearity / Coplanarity")
        print("4. Compute Minor of an Element")
        print("5. Compute Cofactor of an Element")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == '1':
            det = determinant(A)
            print(f"\nDeterminant: {det:.3f}")

        elif choice == '2':
            if inverse_exists(A):
                print("\nInverse exists:")
                print(np.round(get_inverse(A), 3))
            else:
                print("\nMatrix is singular (no inverse).")

        elif choice == '3':
            if A.shape[0] >= 3:
                if check_collinearity(A):
                    print("\nPoints are collinear/coplanar.")
                else:
                    print("\nPoints are not collinear/coplanar.")
            else:
                print("\nThis check requires a 3x3 or larger matrix.")

        elif choice == '4' or choice == '5':
            try:
                r = int(input("Enter row index (1-based): ")) - 1
                c = int(input("Enter column index (1-based): ")) - 1
                if r < 0 or c < 0 or r >= A.shape[0] or c >= A.shape[1]:
                    print("Invalid index.")
                    continue
                if choice == '4':
                    m = get_minor(A, r, c)
                    print(f"\nMinor[{r+1}][{c+1}] = {m:.3f}")
                else:
                    cof = get_cofactor(A, r, c)
                    print(f"\nCofactor[{r+1}][{c+1}] = {cof:.3f}")
            except ValueError:
                print("\nInvalid input. Please enter integer indices.")

        elif choice == '6':
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid choice. Please select from the menu.")

if __name__ == "__main__":
    main()