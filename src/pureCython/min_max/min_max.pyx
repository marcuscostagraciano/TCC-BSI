# cython: language_level=3, boundscheck=False, wraparound=False
cimport numpy as np
from cython cimport Py_ssize_t

cdef extern from 'c_implementations/maxValue_C_implementation.c':
    unsigned long get_max_value_using_C(const unsigned long *array, const size_t size)

cdef extern from 'c_implementations/minValue_C_implementation.c':
    unsigned long get_min_value_using_C(const unsigned long *array, const size_t size)

cdef long double get_max(unsigned long *data_ptr, Py_ssize_t array_size):
    cdef Py_ssize_t i
    cdef unsigned long max = data_ptr[0]

    for i in range(1, array_size):
        if max < data_ptr[i]:
            max = data_ptr[i]
    return max

cdef long double get_min(unsigned long *data_ptr, Py_ssize_t array_size):
    cdef Py_ssize_t i
    cdef unsigned long min = data_ptr[0]

    for i in range(1, array_size):
        if data_ptr[i] < min:
            min = data_ptr[i]
    return min

def get_max_value(np.ndarray[unsigned long, ndim=1] array):
    return get_max(<unsigned long *> array.data, array.size)

def get_min_value(np.ndarray[unsigned long, ndim=1] array):
    return get_min(<unsigned long *> array.data, array.size)

def get_max_using_c(np.ndarray[unsigned long, ndim=1] array):
    return get_max_value_using_C(<unsigned long *> array.data, array.size)

def get_min_using_c(np.ndarray[unsigned long, ndim=1] array):
    return get_min_value_using_C(<unsigned long *> array.data, array.size)
