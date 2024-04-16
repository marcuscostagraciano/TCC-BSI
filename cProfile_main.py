# flake8: noqa
# import timeit
from purePython import fibonacci_pure_python as pure_python
from compiledPython import fibonacci_compiled_python as compiled_python
from compiled_pythonTYPED import fibonacci_compiledTYPED_python as compiled_typed
from pureCython import fibonacci_pure_cython as pure_cython

n_teste = int(1_000_000)
# n_calls: int = 1_000

# pure_python(n_teste)
# compiled_python(n_teste)
compiled_typed(n_teste)
pure_cython(n_teste)
