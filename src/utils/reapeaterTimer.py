import time
import timeit
from typing import Callable

import numpy as np

from src.pureCython import (
    get_amplitude, get_amplitude_using_C_minMax, get_max_using_c,
    get_max_value, get_mean, get_min_using_c, get_min_value
)

from . import ARRAY_NUMEROS, NUM_REGISTROS, NUM_REPETICOES

NP_FUNCTIONS: dict[str, str] = {
    "max": "np.max",
    "min": "np.min",
    "var": "np.var",
    "ptp": "np.ptp",
    "mean": "np.mean",
}


def repeaterTimer(
    # Força o uso de parâmetros nomeados (kwargs)
    *,
    function: Callable[..., float],
    repeatTimes: int | None = None,
    number: int = 1,
    # perf_counter() é o timer padrão utilizado pelo módulo. Fonte: https://docs.python.org/3/library/timeit.html#timeit.default_timer
    timer: Callable[..., float] = time.perf_counter_ns,
) -> list[int | float]:
    """Função usada para retornar a lista de medições de tempo com base na função passada como argumento.

    Args:
            function (Callable): Função a ser cronometrada.
            repeatTimes (int): Número de medições feitas.
            number (int, optional): Número de execuções da função por medição. Padrão = 1.
            timer (Callable, optional): Timer usado para cronometrar a função. Usa, por padrão, o método perf_counter_ns.

    Returns:
            list[int | float]: Lista contendo o(s) tempo(s) da(s) medição(ões).
    """
    # Se não for passado, usa o padrão definido no arquivo de constantes
    repeatTimes = NUM_REPETICOES if repeatTimes is None else repeatTimes

    # Pega o nome da função
    dunder_function_name = function.__name__
    # Usa a função do NumPy se existir no dicionário, senão mantém a original.
    function_name = (
        dunder_function_name
        if dunder_function_name not in NP_FUNCTIONS
        else NP_FUNCTIONS[dunder_function_name]
    )

    print(
        f"Quantidade de números inspecionados: {NUM_REGISTROS * repeatTimes * number:_}"
    )
    print(f"{function_name} iniciada - ", end="")

    t1 = time.time()
    lista_tempos: list[float] = timeit.repeat(
        # Define dinamicamente o nome da função a ser executada
        f"{function_name}(ARRAY_NUMEROS)",
        # Permite que a função "repeat" olhe no namespace global
        globals=globals(),
        # Quantas vezes as medições serão feitas
        repeat=repeatTimes,
        # Número de execuções por medição
        number=number,
        timer=timer,
    )
    t2 = time.time()

    print(f"{function_name} terminada após {t2 - t1:.5f}s")

    return lista_tempos
