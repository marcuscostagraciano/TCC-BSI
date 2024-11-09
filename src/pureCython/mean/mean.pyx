# cython: language_level=3, boundscheck=False, wraparound=False
cimport cython
cimport numpy as np
from cython cimport Py_ssize_t

@cython.boundscheck(False)
@cython.wraparound(False)
cdef unsigned long get_mean_value_cython(np.ndarray[unsigned long, ndim=1] array):
    cdef unsigned long *data_ptr = <unsigned long *> array.data
    cdef Py_ssize_t array_size = array.size
    cdef unsigned long sum_array_values = 0

    for i in range(array_size):
        sum_array_values += data_ptr[i]

    return sum_array_values / array_size

def get_mean_value_py_wrapper(np.ndarray[unsigned long, ndim=1] array):
    return get_mean_value_cython(array)
