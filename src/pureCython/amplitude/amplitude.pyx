# cython: language_level=3, boundscheck=False, wraparound=False
cimport numpy as np
from cython cimport Py_ssize_t

cdef extern from '../min_max/c_implementations/maxValue_C_implementation.c':
    unsigned long get_max_value_using_C(const unsigned long *array, const size_t size)

cdef extern from '../min_max/c_implementations/minValue_C_implementation.c':
    unsigned long get_min_value_using_C(const unsigned long *array, const size_t size)

cdef unsigned long get_amplitude_cython(unsigned long *data_ptr, Py_ssize_t array_size):
    cdef Py_ssize_t i
    cdef unsigned long min_value = data_ptr[0], max_value = data_ptr[0]

    for i in range(1, array_size):
        if data_ptr[i] < min_value:
            min_value = data_ptr[i]
        elif max_value < data_ptr[i]:
            max_value = data_ptr[i]

    return max_value - min_value


def get_amplitude(np.ndarray[unsigned long, ndim=1] array):
    return get_amplitude_cython(<unsigned long *> array.data, array.size)

def get_amplitude_using_C_minMax(np.ndarray[unsigned long, ndim=1] array):
    return get_max_value_using_C(<unsigned long *> array.data, array.size) - get_min_value_using_C(<unsigned long *> array.data, array.size)
