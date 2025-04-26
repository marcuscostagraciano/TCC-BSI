import time
from funcao_lenta import funcao_lenta

tempo_inicial: float = time.perf_counter()
resultado: str = funcao_lenta(1_000_000)
tempo_final: float = time.perf_counter()

print(f'Concatenações de {1_000_000:_} números')
print(f'{resultado[:10] = }...') # Impressão dos 10 primeiros dígitos
print(f'{tempo_final - tempo_inicial = :.5f}s')