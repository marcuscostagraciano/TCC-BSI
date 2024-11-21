# cython: language_level=3, boundscheck=False, wraparound=False
cimport cython
cimport numpy as np
from cython cimport Py_ssize_t

@cython.boundscheck(False)
@cython.wraparound(False)
cdef long double get_variance_cython(
    unsigned long *data_ptr, Py_ssize_t array_size, short ddof
    ):
    cdef Py_ssize_t i
    cdef long double mean, array_sum = 0, array_sum2 = 0

    for i in range(0, array_size):
        array_sum += data_ptr[i]
    mean = array_sum / array_size

    for i in range(0, array_size):
        array_sum2 += (data_ptr[i] - mean) ** 2
    return array_sum2 / (array_size - ddof)


def get_variance(np.ndarray[unsigned long, ndim=1] array, bint ddof=0):
    # 'ddof' comes from: https://numpy.org/doc/stable/reference/generated/numpy.var.html
    return get_variance_cython(<unsigned long *> array.data, array.size, ddof)
