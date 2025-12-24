from matrix_karavictor import Matrix
import numpy as np


def main():
    np.random.seed(0)

    a = Matrix(np.random.randint(0, 10, (10, 10)))
    b = Matrix(np.random.randint(0, 10, (10, 10)))

    (a + b).save("matrix_2_add.txt")
    (a * b).save("matrix_2_mul.txt")
    (a @ b).save("matrix_2_matmul.txt")


if __name__ == "__main__":
    main()

if __name__ == '__main__':
    main()
