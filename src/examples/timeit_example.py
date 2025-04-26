import time
import timeit

NUMEROS_A_SEREM_CONCATENADOS: int = 1_000_000
REPETICOES: int = 15

def funcao_lenta(entrada: int) -> str:
    resultado: str = ""
    for _ in range(entrada):
        resultado += str(_)
    return resultado

temporizadores: list[float] = timeit.repeat(
    # Chama a função "funcao_lenta" passando os valores presentes na constante "NUMEROS_A_SEREM_CONCATENADOS".
    f"funcao_lenta({NUMEROS_A_SEREM_CONCATENADOS})",
    # Permite que a função "repeat" tenha acesso à função "funcao_lenta".
    globals=globals(),
    # Define o timer usado pela função "repeat". O padrão já é o "perf_counter".
    timer=time.perf_counter,
    # Número de medições realizadas.
    repeat=REPETICOES,
    # Número de repetições de chamada da "funcao_lenta" por medição.
    number=1,
)

print(f"Concatenações de {NUMEROS_A_SEREM_CONCATENADOS:_} números. {REPETICOES} repetições")
# Arredonda o número para conter 5 dígitos decimais
print(f"{[round(tempo, 5) for tempo in temporizadores]}")
