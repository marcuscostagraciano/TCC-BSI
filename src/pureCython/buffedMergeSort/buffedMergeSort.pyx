# cython: language_level=3, boundscheck=False, wraparound=False, profile=True
from cython cimport Py_ssize_t
cimport numpy as cnp
from libc.stdlib cimport malloc, free


# Implementação mais rápida usando memoryviews e alocação de memória C
cdef void merge_mv(
        cnp.uint32_t[:] array,
        Py_ssize_t left, Py_ssize_t mid,
        Py_ssize_t right
    ):
    cdef Py_ssize_t i, j, n1 = mid - left + 1, n2 = right - mid, k = left
    cdef cnp.uint32_t *L = <cnp.uint32_t *>malloc(n1 * sizeof(cnp.uint32_t))
    cdef cnp.uint32_t *R = <cnp.uint32_t *>malloc(n2 * sizeof(cnp.uint32_t))

    for i in range(n1):
        L[i] = array[left + i]
    for j in range(n2):
        R[j] = array[mid + 1 + j]

    i = 0
    j = 0

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        array[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        array[k] = R[j]
        j += 1
        k += 1

    free(L)
    free(R)


cdef void merge_sort_mv(
        cnp.uint32_t[:] array,
        Py_ssize_t left,
        Py_ssize_t right
    ):
    cdef Py_ssize_t mid = (left + right) // 2

    if left < right:
        merge_sort_mv(array, left, mid)
        merge_sort_mv(array, mid + 1, right)
        merge_mv(array, left, mid, right)


def py_merge_sort_fast(
        cnp.uint32_t[:] array
    ):
    merge_sort_mv(array, 0, array.size - 1)
    return array
