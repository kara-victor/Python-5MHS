import numpy as np
from numpy.lib.mixins import NDArrayOperatorsMixin


class FileSaveMixin:
    def save(self, filename):
        with open(filename, "w", encoding="utf-8") as f:
            f.write(str(self))


class PrintMixin:
    def __str__(self):
        return "\n".join("\t".join(map(str, row)) for row in self._data)


class AccessMixin:
    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, value):
        arr = np.array(value)
        self._data = arr

    def shape(self):
        return self._data.shape


class Matrix(
    NDArrayOperatorsMixin,
    FileSaveMixin,
    PrintMixin,
    AccessMixin,
):
    def __init__(self, data):
        self.data = data

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        processed_inputs = []
        for x in inputs:
            if isinstance(x, Matrix):
                processed_inputs.append(x._data)
            else:
                return NotImplemented

        result = getattr(ufunc, method)(*processed_inputs, **kwargs)

        if isinstance(result, tuple):
            return tuple(Matrix(x) for x in result)

        return Matrix(result)
