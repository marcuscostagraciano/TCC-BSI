import time

NUMEROS_A_SEREM_CONCATENADOS: int = 1_000_000

def funcao_lenta(entrada: int) -> str:
    resultado: str = ""
    for _ in range(entrada):
        resultado += str(_)
    return resultado

# Captura inicial do contador
tempo_inicial: float = time.perf_counter()
# Execução de um código (propositalmente) lento
resultado: str = funcao_lenta(NUMEROS_A_SEREM_CONCATENADOS)
# Captura final do contador
tempo_final: float = time.perf_counter()

print(f"Concatenações de {NUMEROS_A_SEREM_CONCATENADOS:_} números")
# Impressão dos 10 primeiros dígitos do resultado
print(f"{resultado[:10] = }...")
# Impressão da diferença de tempo entre as capturas dos contadores
print(f"{tempo_final - tempo_inicial = :.5f}s")
