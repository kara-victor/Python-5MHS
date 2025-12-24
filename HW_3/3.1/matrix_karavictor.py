import numpy as np


class Matrix:
    def __init__(self, data):
        self.data = np.array(data)

    def shape(self):
        return self.data.shape

    def __add__(self, other):
        if self.shape() != other.shape():
            raise ValueError(
                f"Cannot add matrices with {self.shape()} and {other.shape()}"
            )

        return Matrix(self.data + other.data)

    def __matmul__(self, other):
        if self.shape()[1] != other.shape()[0]:
            raise ValueError(
                f"Cannot do matrix multiplication for {self.shape()} and {other.shape()}"
            )

        return Matrix(self.data @ other.data)

    def __mul__(self, other):
        if self.shape() != other.shape():
            raise ValueError(
                f"Cannot do element-wise multiplication for {self.shape()} and {other.shape()}"
            )

        return Matrix(self.data * other.data)

    def __str__(self):
        return "\n".join("\t".join(map(str, row)) for row in self.data)
