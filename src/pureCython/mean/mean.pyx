# cython: language_level=3, boundscheck=False, wraparound=False
cimport cython
cimport numpy as np
from cython cimport Py_ssize_t

@cython.boundscheck(False)
@cython.wraparound(False)
cdef long double get_mean_value_cython(unsigned long *data_ptr, Py_ssize_t array_size):
    cdef Py_ssize_t i
    cdef unsigned long long sum_array_values = 0

    for i in range(array_size):
        sum_array_values += data_ptr[i]
    
    return sum_array_values / array_size

def get_mean(np.ndarray[unsigned long, ndim=1] array):
    return get_mean_value_cython(<unsigned long *> array.data, array.size)
