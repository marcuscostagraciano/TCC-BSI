import cython


def fibonacci_compiled_python(number: cython.int) -> cython.ulong:
    """ Fibonacci implementation in default CPython and compiled after with
        static typing """
    a: cython.ulong = 0
    b: cython.ulong = 1

    for i in range(number):
        a, b = a + b, a

    return a
