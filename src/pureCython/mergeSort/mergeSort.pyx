# cython: language_level=3, boundscheck=False, wraparound=False, profile=True
# cimport cython
from cython cimport Py_ssize_t
cimport numpy as cnp


cdef void merge(
        cnp.ndarray[unsigned long, ndim=1] array,
        Py_ssize_t left,
        Py_ssize_t mid,
        Py_ssize_t right
    ):
    # Calcula o tamanho dos subarrays esquerdo (n1) e direito (n2)
    cdef Py_ssize_t i, j, n1 = mid - left + 1, n2 = right - mid, k = left
    # Obtém um ponteiro para os dados do array original para acesso eficiente
    cdef unsigned long *data_ptr = <unsigned long *> array.data

    cdef unsigned long[:] L = cnp.PyArray_ZEROS(1, [n1], cnp.NPY_UINT32, False), R = cnp.PyArray_ZEROS(1, [n2], cnp.NPY_UINT32, False)

    for i in range(n1):
        L[i] = data_ptr[left + i]
    for j in range(n2):
        R[j] = data_ptr[mid + 1 + j]

    i = 0; j = 0

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            data_ptr[k] = L[i]
            i += 1
        else:
            data_ptr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        data_ptr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        data_ptr[k] = R[j]
        j += 1
        k += 1


cdef void merge_sort(
        cnp.ndarray[unsigned long, ndim=1] array,
        Py_ssize_t left,
        Py_ssize_t right
    ):
    # Calcula o índice do meio do subarray
    cdef Py_ssize_t mid = (left + right) // 2

    # Se ainda há mais de um elemento, divide e ordena recursivamente
    if left < right:
        merge_sort(array, left, mid)		# Ordena a metade esquerda
        merge_sort(array, mid + 1, right)	# Ordena a metade direita
        merge(array, left, mid, right)		# Mescla as duas metades ordenadas


def py_merge_sort(cnp.ndarray[unsigned long, ndim=1] array):
    # Chama a função de ordenação merge_sort com os índices apropriados
    merge_sort(array, 0, array.size - 1)
    return array
