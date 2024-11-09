from time import perf_counter
from typing import Final

import numpy as np

from src import get_mean_value_cython

# from src.cPython import testingFunctions

# NUM_REGISTROS: Final[int] = 4.5 * 10**9
NUM_REGISTROS: Final[int] = 0.1 * 10**9
NUM_REGISTROS: Final[int] = 1 * 10**9

start_time = perf_counter()
ARRAY_NUMEROS = np.arange(NUM_REGISTROS, dtype=np.uint32)
end_time = perf_counter()

print(f"{ARRAY_NUMEROS.size = :,}")
print(f"Array creation timing: {end_time - start_time:.5f}s\n")

# start_time = perf_counter()
# get_max_value_C_result = get_max_value_C(ARRAY_NUMEROS)
# end_time = perf_counter()

# print(f"get_max_value_C timing: {end_time - start_time:.5f}s")
# print(f"get_max_value_C result: {get_max_value_C_result}")

# start_time = perf_counter()
# get_max_value_numpy_result = np.max(ARRAY_NUMEROS)
# end_time = perf_counter()

# print(f"get_max_value_numpy timing: {end_time - start_time:.5f}s")
# print(f"get_max_value_numpy result: {get_max_value_numpy_result}")

sttime = perf_counter()
np_amplitude_result = np.ptp(ARRAY_NUMEROS)
edtime = perf_counter()
print(f"np_amplitude timing: {edtime - sttime:.5f}s")
print(f"np_amplitude result: {np_amplitude_result}")

# sttime = perf_counter()
# amplitude_w_python_functions_result = testingFunctions.amplitude_w_python_functions(
#     ARRAY_NUMEROS
# )
# edtime = perf_counter()
# print(f"amplitude_w_python_functions timing: {edtime - sttime:.5f}s")
# print(f"amplitude_w_python_functions result: {amplitude_w_python_functions_result}")

# sttime = perf_counter()
# py_amplitude_result = testingFunctions.amplitude(ARRAY_NUMEROS)
# edtime = perf_counter()
# print(f"py_amplitude timing: {edtime - sttime:.5f}s")
# print(f"py_amplitude result: {py_amplitude_result}")


# MUST DO
# AVERAGE

# MEAN
sttime = perf_counter()
np_mean_value_result = np.mean(ARRAY_NUMEROS)
edtime = perf_counter()
print(f"np_mean_value timing: {edtime - sttime:.5f}s")
print(f"np_mean_value result: {np_mean_value_result}")

sttime = perf_counter()
cy_mean_value_result = get_mean_value_cython(ARRAY_NUMEROS)
edtime = perf_counter()
print(f"cy_mean_value timing: {edtime - sttime:.5f}s")
print(f"cy_mean_value result: {cy_mean_value_result}")

# STD (STANDARD DEVIATION)
# VAR (VARIANCE)
# AMPLITUDE
