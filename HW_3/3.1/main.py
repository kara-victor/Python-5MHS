from matrix_karavictor import Matrix
import numpy as np


def save_matrix(filename, matrix):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(str(matrix))


def main():
    np.random.seed(0)

    a = Matrix(np.random.randint(0, 10, (10, 10)))
    b = Matrix(np.random.randint(0, 10, (10, 10)))

    add_result = a + b
    mul_result = a * b
    matmul_result = a @ b

    save_matrix("matrix_plus.txt", add_result)
    save_matrix("matrix_mul.txt", mul_result)
    save_matrix("matrix_matmul.txt", matmul_result)


if __name__ == '__main__':
    main()
