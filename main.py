from time import perf_counter
from typing import Final

import numpy as np

from src import (
    get_amplitude_cython,
    get_max_using_numpy,
    get_max_value,
    get_mean_value_cython,
    get_min_using_numpy,
    get_min_value,
    get_variance,
)

# from src.cPython import testingFunctions

# NUM_REGISTROS: Final[int] = 4.5 * 10**9
NUM_REGISTROS: Final[int] = 0.1 * 10**9
# NUM_REGISTROS: Final[int] = 1 * 10**9

start_time = perf_counter()
ARRAY_NUMEROS = np.arange(NUM_REGISTROS, dtype=np.uint32)
end_time = perf_counter()

print(f"{ARRAY_NUMEROS.size = :,}")
print(f"Array creation timing: {end_time - start_time:.5f}s\n")

# MUST DO
# AMPLITUDE
sttime = perf_counter()
cy_amplitude_result = get_amplitude_cython(ARRAY_NUMEROS)
edtime = perf_counter()
print(f"cy_amplitude timing: {edtime - sttime:.5f}s")
print(f"cy_amplitude result: {cy_amplitude_result}")

sttime = perf_counter()
np_amplitude_result = np.ptp(ARRAY_NUMEROS)
edtime = perf_counter()
print(f"np_amplitude timing: {edtime - sttime:.5f}s")
print(f"np_amplitude result: {np_amplitude_result}\n")


# MAX
sttime = perf_counter()
get_max_value_result = get_max_value(ARRAY_NUMEROS)
edtime = perf_counter()
print(f"get_max_value timing: {edtime - sttime:.5f}s")
print(f"get_max_value result: {get_max_value_result}")

sttime = perf_counter()
max_result = np.max(ARRAY_NUMEROS)
edtime = perf_counter()
print(f"max timing: {edtime - sttime:.5f}s")
print(f"max result: {max_result}\n")


# MIN
sttime = perf_counter()
get_min_value_result = get_min_value(ARRAY_NUMEROS)
edtime = perf_counter()
print(f"get_min_value timing: {edtime - sttime:.5f}s")
print(f"get_min_value result: {get_min_value_result}")

sttime = perf_counter()
min_result = np.min(ARRAY_NUMEROS)
edtime = perf_counter()
print(f"min timing: {edtime - sttime:.5f}s")
print(f"min result: {min_result}\n")


# MEAN (arithmetic mean)
sttime = perf_counter()
cy_mean_value_result = get_mean_value_cython(ARRAY_NUMEROS)
edtime = perf_counter()
print(f"cy_mean_value timing: {edtime - sttime:.5f}s")
print(f"cy_mean_value result: {cy_mean_value_result}")

sttime = perf_counter()
np_mean_value_result = np.mean(ARRAY_NUMEROS)
edtime = perf_counter()
print(f"np_mean_value timing: {edtime - sttime:.5f}s")
print(f"np_mean_value result: {np_mean_value_result}\n")


# VAR (VARIANCE)
sttime = perf_counter()
cy_variance_result = get_variance(ARRAY_NUMEROS)
edtime = perf_counter()
print(f"cy_variance timing: {edtime - sttime:.5f}s")
print(f"cy_variance result: {cy_variance_result}")

sttime = perf_counter()
np_var_result = np.var(ARRAY_NUMEROS)
edtime = perf_counter()
print(f"np_var timing: {edtime - sttime:.5f}s")
print(f"np_var result: {np_var_result}\n")


# STD (STANDARD DEVIATION)
