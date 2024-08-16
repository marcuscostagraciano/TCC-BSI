# cython: language_level=3, boundscheck=False, wraparound=False
cimport cython
cimport numpy as np

cdef extern from "get_max_value_C_implementation.c":
    unsigned long get_max_value(const unsigned long *array, size_t size)

@cython.boundscheck(False)
@cython.wraparound(False)
cdef unsigned long get_max_value_C_function(np.ndarray[unsigned long, ndim=1] array):
    cdef unsigned long *data_ptr = <unsigned long *> array.data
    return get_max_value(data_ptr, array.size)

def get_max_value_using_C_implementation(
    np.ndarray[unsigned long, ndim=1] array
):
    return get_max_value_C_function(array)
