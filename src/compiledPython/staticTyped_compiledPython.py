import cython


def fibonacci_compiled_python(number: cython.int) -> cython.double:
    """ Fibonacci implementation in default CPython and compiled after with
        static typing """
    a: cython.double = 0
    b: cython.double = 1

    for i in range(number):
        a, b = a + b, a

    return a
