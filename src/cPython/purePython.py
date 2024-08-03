def fibonacci_pure_python(number: int) -> int:
    """ Fibonacci implementation in default CPython """
    a: int = 0
    b: int = 1

    for i in range(number):
        a, b = a + b, a

    return a
