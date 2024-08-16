import time
from typing import Final

import numpy as np
from numpy import ndarray

NUM_REGISTROS: Final[int] = 4.5 * 10**9

# start_time = time.perf_counter()
# # ARRAY_NUMEROS: ndarray = np.arange(NUM_REGISTROS, dtype=np.uint16)
# ARRAY_NUMEROS: ndarray = np.arange(NUM_REGISTROS, dtype=np.uint32)
# stop_time = time.perf_counter()
# print(f"Elapsed ARANGE time: {stop_time - start_time:.3f}s")

# start_time = time.perf_counter()
# min_value_from_array = np.min(ARRAY_NUMEROS)
# stop_time = time.perf_counter()
# print(f"Elapsed MIN time: {stop_time - start_time:.3f}s")

# start_time = time.perf_counter()
# max_value_from_array = np.max(ARRAY_NUMEROS)
# stop_time = time.perf_counter()
# print(f"Elapsed MAX time: {stop_time - start_time:.3f}s")

from src.pureCython import create_array_wrapper

# from src.pureCython.handle_array import create_array_wrapper

create_array_wrapper(NUM_REGISTROS)
