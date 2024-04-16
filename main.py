# flake8: noqa
import timeit
from purePython import fibonacci_pure_python as pure_python
# from fib_cytCpy import fibonacci_py as python_cython_fib
# from fib_cython import calc_fibonacci_cy as pure_cython_fib
# from tabulate import tabulate
# import pandas as pd

# Run tests multiple times and calculate average
# n_teste = int(input("Fib number: "))
n_teste = int(1_000_000)
n_calls: int = 1_000

print(f"{n_calls:_} calls for each function\n")
# print(f"fibonnaci: {pure_cython_fib(n_teste):_}")


pure_python_time = timeit.timeit(lambda: pure_python(n_teste), number=n_calls)
# compiled_python_time = timeit.timeit(lambda: pure_compiled_fib(n_teste), number=n_calls)
# cythonized_python_time = timeit.timeit(lambda: python_cython_fib(n_teste), number=n_calls)
# pure_cython_time = timeit.timeit(lambda: pure_cython_fib(n_teste), number=n_calls)

print(f"Pure Python time: {pure_python_time:.5f} seconds")
# print(f"Compiled python time: {compiled_python_time:.5f} seconds")
# print(f"Cython Type Annoted Python time: {cythonized_python_time:.5f} seconds")
# print(f"Pure cython time: {pure_cython_time:.5f} seconds")
# print("")
# print(f"compiled python: {compiled_python_time/pure_python_time:.5f}x")
# print(f"compiled python + type hint: {cythonized_python_time/pure_python_time:.5f}x")
# print(f"pure cython: {pure_cython_time/pure_python_time:.5f}x")

# df = pd.DataFrame({
#     "code_type": ["cpython_timing", "compiled_wo_typing", "compiled_w_typing", "cython"],
#     "timings": [a := timeit.timeit(lambda: fibonacci_python_puro(n_teste), number=n_calls),
#                 b := timeit.timeit(lambda: pure_compiled_fib(n_teste), number=n_calls),
#                 c := timeit.timeit(lambda: python_cython_fib(n_teste), number=n_calls),
#                 d := timeit.timeit(lambda: pure_cython_fib(n_teste), number=n_calls)],
#     "times_faster": [
#         f"{a/a:.5f}",
#         f"{b/a:.5f}",
#         f"{c/a:.5f}",
#         f"{d/a:.5f}",
#     ]
# })
# print(tabulate(df, headers = 'keys', tablefmt = 'fancy_grid'))
