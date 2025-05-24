import numpy as np
import pandas as pd

from src.pureCython import (
    get_amplitude, get_amplitude_using_C_minMax, get_max_using_c,
    get_max_value, get_mean, get_min_using_c, get_min_value
)
from src.classes import GraphConfig, LinePlot, ViolinPlot
from src.utils.reapeaterTimer import repeaterTimer


class BaseTests:
    __download: bool = False
    __only_download: bool = True
    __download_folder: str = ""


    @classmethod
    def generate_graph(
            cls,
            config: GraphConfig
        ) -> None:
        """Função usada para gerar os gráficos dos testes.

        Args:
            config (GraphConfig): Objeto contendo as informações necessárias para a geração do gráfico.
        """

        # Verifica se o download dos gráficos é necessário
        if cls.__download or cls.__only_download:
            LinePlot(config).download(cls.__download_folder)
            ViolinPlot(config).download(cls.__download_folder)
        if not cls.__only_download:
            LinePlot(config).generate()
            ViolinPlot(config).generate()


    @classmethod
    def set_download(
            cls,
            download: bool = False,
            download_folder: str = '',
            only_download: bool = True
        ) -> type['BaseTests']:
        """Função usada para definir se os gráficos devem ser salvos e o caminho onde serão salvos.

        Args:
            download (bool, optional): Se True, salva os gráficos gerados.
            download_folder (str, optional): Caminho onde os gráficos serão salvos.
            only_download (bool, opcional): Se True, salva os gráficos sem exibi-los.
        """
        cls.__download = download
        cls.__only_download = only_download
        cls.__download_folder = download_folder

        return cls


class Tests(BaseTests):
    """Classe usada para realizar os testes de desempenho."""
    # Variáveis usadas para armazenar os tempos de execução do NumPy (utilizadas em mais de um teste)
    __tempos_numpy_max: list[float] | None = None
    __tempos_numpy_min: list[float] | None = None
    __tempos_numpy_ptp: list[float] | None = None
    


    @classmethod
    def get_max_value_using_c(cls):
        """Função usada para medir o tempo de execução da função get_max_using_c e compará-la com a função np.max do NumPy."""
        cls.generate_graph(
            GraphConfig(
                title = "Valor máximo - C x NumPy",
                loc = "upper right",
                timings_data = pd.DataFrame(
                    data = {
                        "C": repeaterTimer(function=get_max_using_c),
                        "NumPy": (tempos_numpy_max := repeaterTimer(function=np.max)),
                    }
                )
            )
        )
        cls.__tempos_numpy_max = tempos_numpy_max


    @classmethod
    def get_max_value_using_cython(cls):
        """Função usada para medir o tempo de execução da função get_max_value e compará-la com a função np.max do NumPy."""
        cls.generate_graph(
            GraphConfig(
                title = "Valor máximo - Cython x NumPy",
                loc = "upper right",
                timings_data = pd.DataFrame(
                    data = {
                        "Cython": repeaterTimer(function=get_max_value),
                        "NumPy": cls.__tempos_numpy_max,
                    }
                ),
            )
        )


    @classmethod
    def get_min_value_using_c(cls):
        """Função usada para medir o tempo de execução da função get_min_using_c e compará-la com a função np.min do NumPy."""
        cls.generate_graph(
            GraphConfig(
                title = "Valor mínimo - C x NumPy",
                loc = "upper right",
                timings_data = pd.DataFrame(
                    data = {
                        "C": repeaterTimer(function=get_min_using_c),
                        "NumPy": (tempos_numpy_min := repeaterTimer(function=np.min)),
                    }
                )
            )
        )
        cls.__tempos_numpy_min = tempos_numpy_min


    @classmethod
    def get_min_value_using_cython(cls):
        """Função usada para medir o tempo de execução da função get_min_value e compará-la com a função np.min do NumPy."""
        cls.generate_graph(
            GraphConfig(
                title = "Valor mínimo - Cython x NumPy",
                loc = "upper right",
                timings_data = pd.DataFrame(
                    data = {
                        "Cython": repeaterTimer(function=get_min_value),
                        "NumPy": cls.__tempos_numpy_min,
                    }
                )
            )
        )


    @classmethod
    def get_mean_using_cython(cls):
        """Função usada para medir o tempo de execução da função get_mean e compará-la com a função np.mean do NumPy."""
        cls.generate_graph(
            GraphConfig(
                title = "Média aritmética - Cython x NumPy",
                timings_data = pd.DataFrame(
                    data = {
                        "Cython": repeaterTimer(function=get_mean),
                        "NumPy": repeaterTimer(function=np.mean)
                    }
                )
            )
        )


    @classmethod
    def get_amplitude_using_c(cls):
        """Função usada para medir o tempo de execução da função get_amplitude_using_C_minMax e compará-la com a função np.ptp do NumPy."""
        cls.generate_graph(
            GraphConfig(
                title = "Amplitude - C x NumPy",
                loc = "upper right",
                timings_data = pd.DataFrame(
                    data = {
                        "C": repeaterTimer(function=get_amplitude_using_C_minMax),
                        "NumPy": (tempos_numpy_ptp := repeaterTimer(function=np.ptp)),
                    }
                )
            )
        )
        cls.__tempos_numpy_ptp = tempos_numpy_ptp


    @classmethod
    def get_amplitude_using_cython(cls):
        """Função usada para medir o tempo de execução da função get_amplitude e compará-la com a função np.ptp do NumPy."""
        cls.generate_graph(
            GraphConfig(
                title = "Amplitude - Cython x NumPy",
                loc = "upper right",
                timings_data = pd.DataFrame(
                    data = {
                        "Cython": repeaterTimer(function=get_amplitude),
                        "NumPy": cls.__tempos_numpy_ptp,
                    }
                )
            )
        )


    @classmethod
    def run_max_value_tests(cls) -> type['Tests']:
        """Função usada para executar os testes de valor máximo."""
        cls.get_max_value_using_c()
        cls.get_max_value_using_cython()

        return cls


    @classmethod
    def run_min_value_tests(cls) -> type['Tests']:
        """Função usada para executar os testes de valor mínimo."""
        cls.get_min_value_using_c()
        cls.get_min_value_using_cython()

        return cls


    @classmethod
    def run_mean_value_tests(cls) -> type['Tests']:
        """Função usada para executar os testes de média aritmética."""
        cls.get_mean_using_cython()

        return cls


    @classmethod
    def run_amplitude_tests(cls) -> type['Tests']:
        """Função usada para executar os testes de amplitude."""
        cls.get_amplitude_using_c()
        cls.get_amplitude_using_cython()

        return cls


    @classmethod
    def run_all_tests(cls) -> type['Tests']:
        """Função usada para executar todos os testes de desempenho."""
        cls.run_max_value_tests()
        cls.run_min_value_tests()
        cls.run_mean_value_tests()
        cls.run_amplitude_tests()

        return cls
