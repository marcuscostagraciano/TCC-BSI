from typing import Final

import numpy as np

# Número de vezes que as medições serão executadas
NUM_REPETICOES: Final[int] = 1_000

# Quantidade de números usados para os testes
# NUM_REGISTROS: Final[int] = int(4.5 * 10**9)
NUM_REGISTROS: Final[int] = int(0.20 * 10**9)

# Array NumPy contendo os números para os testes
ARRAY_NUMEROS = np.arange(NUM_REGISTROS, dtype=np.uint32)

print(f"{ARRAY_NUMEROS.size = :,}")
