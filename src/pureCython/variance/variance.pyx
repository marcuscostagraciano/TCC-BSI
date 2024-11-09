# cython: language_level=3, boundscheck=False, wraparound=False
cimport cython
cimport numpy as np
from cython cimport Py_ssize_t

@cython.boundscheck(False)
@cython.wraparound(False)
cdef long double get_variance(
    unsigned long *data_ptr,
    Py_ssize_t array_size,
    bint ddof
    ):
    cdef Py_ssize_t i
    cdef long double array_sum = 0
    
    print(ddof)
    print(array_size - ddof)
    # for i in range(array_size):
    #     array_sum += (data_ptr[i] - array_mean) ** 2
    
    # Formula from: https://numpy.org/doc/stable/reference/generated/numpy.var.html
    return array_sum / (array_size - ddof)

    cdef long double sum_x = 0.0  # Sum of the data points
    cdef long double sum_x2 = 0.0  # Sum of the squared data points

    # Calculate the sum and sum of squares in one pass
    for i in range(array_size):
        sum_x += data_ptr[i]
        sum_x2 += data_ptr[i] ** 2
    
    # Calculate mean and variance in one pass
    mean = sum_x / array_size
    var = (sum_x2 / array_size) - (mean ** 2)
    
    return var


def get_variance_py_wrapper(np.ndarray[unsigned long, ndim=1] array, bint ddof=0):
    return get_variance(<unsigned long *> array.data, array.size, ddof)
