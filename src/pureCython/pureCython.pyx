# Cython
def fibonacci_pure_cython(int n):
    """ Compiled and typed Cython code """
    cdef int i
    cdef unsigned long a = 0
    cdef unsigned long b = 1

    for i in range(n):
        a, b = a + b, a

    return a
