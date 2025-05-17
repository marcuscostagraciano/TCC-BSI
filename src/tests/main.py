import numpy as np
import pandas as pd

from src import (
    get_amplitude,
    get_amplitude_using_C_minMax,
    get_max_using_c,
    get_max_value,
    get_mean,
    get_min_using_c,
    get_min_value,
)
from src.classes import GraphConfig, LinePlot, ViolinPlot
from src.utils.consts import NUM_REPETICOES
from src.utils.reapeaterTimer import repeaterTimer


def get_max_value_using_c():
    print("Iniciando teste de valor máximo")
    tempos = pd.DataFrame(
        data={
            "C": repeaterTimer(function=get_max_using_c, repeatTimes=NUM_REPETICOES),
            "NumPy": (
                tempos_numpy_max := repeaterTimer(
                    function=np.max, repeatTimes=NUM_REPETICOES
                )
            ),
        }
    )

    config_C_max_value = GraphConfig(timings_data=tempos, loc="upper right")

    ViolinPlot(config_C_max_value, title="Valor máximo - C x NumPy").generate()
    LinePlot(config_C_max_value, title="Valor máximo - C x NumPy").generate()


def get_max_value_using_cython():
    tempos = pd.DataFrame(
        data={
            "Cython": repeaterTimer(function=get_max_value, repeatTimes=NUM_REPETICOES),
            "NumPy": tempos_numpy_max,
        }
    )

    config_Cython_max_value = GraphConfig(timings_data=tempos, loc="upper right")
    ViolinPlot(
        config_Cython_max_value, title="Valor máximo - Cython x NumPy"
    ).generate()
    LinePlot(config_Cython_max_value, title="Valor máximo - Cython x NumPy").generate()
