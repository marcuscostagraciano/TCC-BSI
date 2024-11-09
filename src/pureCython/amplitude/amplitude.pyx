# cython: language_level=3, boundscheck=False, wraparound=False
cimport cython
cimport numpy as np
from cython cimport Py_ssize_t
# from numpy import ptp

# @cython.boundscheck(False)
# @cython.wraparound(False)
# cdef unsigned long get_amplitude_cython_and_numpy(np.ndarray[np.uint32_t, ndim=1] array):
#     return ptp(array)


@cython.boundscheck(False)
@cython.wraparound(False)
cdef unsigned long get_amplitude_cython(np.ndarray[unsigned long, ndim=1] array):
    cdef const unsigned long *data_ptr = <unsigned long *> array.data
    cdef Py_ssize_t array_size = array.size

    cdef unsigned long i, min_value = data_ptr[0], max_value = data_ptr[0]

    for i in range(1, array_size):
        if data_ptr[i] < min_value:
            min_value = data_ptr[i]
        elif max_value < data_ptr[i]:
            max_value = data_ptr[i]

    return max_value - min_value


def get_amplitude_py_wrapper(np.ndarray[unsigned long, ndim=1] array):
    return get_amplitude_cython(array)
