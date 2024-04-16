from timeit import timeit
from typing import Final

from src import (
    pure_python,
    compiled_notTyped,
    compiled_Typed,
    pure_cython
)

NTH_FIBONACCI_NUMBER: Final[int] = 1_000_000
NUMBER_CALLS: Final[int] = 1_000

python_timing = timeit.timeit(lambda: pure_python(NTH_FIBONACCI_NUMBER),
                              number=NUMBER_CALLS)
compiled = timeit.timeit(lambda: compiled_notTyped(NTH_FIBONACCI_NUMBER),
                         number=NUMBER_CALLS)
compiled_typed = timeit.timeit(lambda: compiled_Typed(NTH_FIBONACCI_NUMBER),
                               number=NUMBER_CALLS)
cython_timing = timeit.timeit(lambda: pure_cython(NTH_FIBONACCI_NUMBER),
                              number=NUMBER_CALLS)

print(f"{python_timing = : .5f}")
print(f"{compiled = : .5f}")
print(f"{compiled_typed = : .5f}")
print(f"{cython_timing = : .5f}")
