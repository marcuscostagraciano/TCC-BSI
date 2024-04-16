def fibonacci_compiled_python(number: int) -> int:
    """ Fibonacci implementation in default CPython and compiled after """
    a: int = 0
    b: int = 1

    for i in range(number):
        a, b = a + b, a

    return a
