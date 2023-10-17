import numpy as np
def input_matrix(rows, columns):
    matrix = np.zeros((rows, columns), dtype=int)
    for i in range(rows):
        for j in range(columns):
            matrix[i][j] = int(input(f"Enter element at position ({i + 1}, {j + 1}): "))
    return matrix

# Input matrices A and B
print("Enter the row and column size of Matrix A:")
m1Row = int(input("Enter the row size: "))
m1Column = int(input("Enter the column size: "))
A = input_matrix(m1Row, m1Column)

print("\nEnter the row and column size of Matrix B:")
m2Row = int(input("Enter the row size: "))
m2Column = int(input("Enter the column size: "))
B = input_matrix(m2Row, m2Column)

if m1Column != m2Column:
    print("Column sizes of Matrix A and Matrix B are not the same. Cannot perform multiplication.")
else:
    # Calculate the product of A and BT
    result = np.dot(A, B.T)

    print("\nMatrix A:")
    print(A)

    print("\nTranspose of Matrix B (BT):")
    print(B.T)

    print("\nProduct of A and BT:")
    print(result)

