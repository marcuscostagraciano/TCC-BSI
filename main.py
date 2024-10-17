import time
from typing import Final

import numpy as np

from src import get_max_value_C

# NUM_REGISTROS: Final[int] = 4.5 * 10**9
NUM_REGISTROS: Final[int] = 2.5 * 10**9

start_time = time.perf_counter()
ARRAY_NUMEROS = np.arange(NUM_REGISTROS, dtype=np.uint32)
end_time = time.perf_counter()

print(f"{ARRAY_NUMEROS.size = :,}")
print(f"Array creation timing: {end_time - start_time:.5f}s\n")

start_time = time.perf_counter()
get_max_value_C_result = get_max_value_C(ARRAY_NUMEROS)
end_time = time.perf_counter()

print(f"get_max_value_C timing: {end_time - start_time:.5f}s")
print(f"get_max_value_C result: {get_max_value_C_result}")

start_time = time.perf_counter()
get_max_value_numpy_result = np.max(ARRAY_NUMEROS)
end_time = time.perf_counter()

print(f"get_max_value_numpy timing: {end_time - start_time:.5f}s")
print(f"get_max_value_numpy result: {get_max_value_numpy_result}")
