import time, timeit
from funcao_lenta import funcao_lenta

print(f'Concatenações de {1_000_000:_} números. {5} repetições')

temporizadores: list[float] = timeit.repeat(
    f'funcao_lenta({1_000_000})',
    globals=globals(),  # Permite que a função 'repeat' tenha acesso à função 'funcao_lenta'.
    timer=time.perf_counter,  # Define o timer usado pela função 'repeat'. O padrão já é o 'perf_counter'.
    repeat=5,  # Número de medições a serem feitas.
    number=1,  # Número de repetições de chamada da 'funcao_lenta' por medição.
)

print(f'{[round(tempo, 5) for tempo in temporizadores]}')