# cython: language_level=3, boundscheck=False, wraparound=False
cimport cython
cimport numpy as np
from cython cimport Py_ssize_t
from numpy import min as np_min, max as np_max

@cython.boundscheck(False)
@cython.wraparound(False)
cdef long double get_max(unsigned long *data_ptr, Py_ssize_t array_size):
    cdef unsigned long i, max = data_ptr[0]
    for i in range(1, array_size):
        if max < data_ptr[i]:
            max = data_ptr[i]
    return max

def get_max_py_wrapper(np.ndarray[unsigned long, ndim=1] array):
    return get_max(<unsigned long *> array.data, array.size)


@cython.boundscheck(False)
@cython.wraparound(False)
cdef long double get_min(unsigned long *data_ptr, Py_ssize_t array_size):
    cdef unsigned long i, min = data_ptr[0]
    for i in range(1, array_size):
        if data_ptr[i] < min:
            min = data_ptr[i]
    return min

def get_min_py_wrapper(np.ndarray[unsigned long, ndim=1] array):
    return get_min(<unsigned long *> array.data, array.size)


def get_max_using_numpy(np.ndarray[unsigned long, ndim=1] array):
    return np_max(array)

def get_min_using_numpy(np.ndarray[unsigned long, ndim=1] array):
    return np_min(array)
