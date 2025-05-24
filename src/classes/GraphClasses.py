"""Classes para geração de gráficos"""
import os
from abc import abstractmethod
from typing import final, Final, Self

import matplotlib.pyplot as plt

from . import GraphConfig


class BaseGraph():
    """Classe base para geração de gráficos."""
    CYTHON_LEGEND_COLOR: Final[str] = "#64a4cc"
    NUMPY_LEGEND_COLOR: Final[str] = "#fb9230"

    def __init__(
        self: Self, graph_config: GraphConfig, *, title: str | None = None
    ) -> None:
        """Função usada para instanciar um objeto da classe específica.

        Args:
                self (Self): Parâmetro passado automaticamente referente ao objeto sendo instanciado.
                graph_config (GraphConfig): Objeto contendo as informações necessárias para a geração do gráfico.
                title (str | None): Se passado, sobrescreve o título do graph_config.
        """
        self.loc = graph_config.loc
        self.grid = graph_config.grid
        self.xlabel = graph_config.xlabel
        self.ylabel = graph_config.ylabel
        self.timings_data = graph_config.timings_data
        self.title = graph_config.title if title is None else title


    def __setGraphInfo(self):
        """Função usada para definir as informações básicas sobre o gráfico."""
        plt.grid(self.grid)
        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)


    @final
    def generate(self):
        """Função usada como "wrapper" de outras funções essenciais para geração dos gráficos."""
        self.__setGraphInfo()
        self._generate()
        plt.show()


    @final
    def downloadGraph(self, download_folder: str) -> None:
        """Função usada para salvar o gráfico gerado.

        Args:
                download_folder (str): Caminho onde o gráfico será salvo.
        """
        download_folder = download_folder if download_folder else "graphs"

        # Verifica se o diretório existe, caso contrário, cria
        os.makedirs(download_folder, exist_ok=True)

        self.__setGraphInfo()
        self._generate()
        plt.savefig(f"{download_folder}/{self.title} - {self.__class__.__name__}.png")
        plt.close()


    @final
    def downloadData(self, download_folder: str) -> None:
        """Função usada para salvar os dados do gráfico gerado.

        Args:
                download_folder (str): Caminho onde os dados serão salvos.
        """
        download_folder = download_folder if download_folder else "data"

        # Verifica se o diretório existe, caso contrário, cria
        os.makedirs(download_folder, exist_ok=True)

        self.timings_data.to_csv(
            f"{download_folder}/{self.title}.csv",
            index=False,
        )


    @abstractmethod
    def _generate(self):
        """Essa função deve ser implementada em cada classe, para definir o tipo de gráfico usado e suas propriedades."""
        pass


class Boxplot(BaseGraph):
    """Classe usada para gerar gráficos de caixa."""

    def _generate(self):
        FACECOLORS: Final[tuple[str, ...]] = ("blue", "purple", "brown", "orange")

        fig, ax = plt.subplots()
        for key, value in enumerate(self.timings_data.columns):
            ax.boxplot(
                self.timings_data[value],
                positions=[key],
                patch_artist=True,
                boxprops={"facecolor": FACECOLORS[key]},
                showfliers=False,
                label=value,
            )

        ax.legend(loc=self.loc)


class ViolinPlot(BaseGraph):
    """Classe usada para gerar gráficos de "violino"."""

    def __init__(
        self: Self,
        graph_config: GraphConfig,
        *,
        title: str | None = None,
        showmeans: bool = True,
        showextrema: bool = True,
    ) -> None:
        """Função usada para instanciar um objeto da classe específica.

        Args:
                self (Self): Parâmetro passado automaticamente referente ao objeto sendo instanciado.
                graph_config (GraphConfig): Objeto contendo as informações necessárias para a geração do gráfico.
                title (str | None): Se passado, sobrescreve o título do graph_config.
                showmeans (bool): Se a mediana deve ser impressa no gráfico.
                showextrema (bool): Se os extremos devem ser impressos no gráfico.
        """
        self.showmeans = showmeans
        self.showextrema = showextrema
        super().__init__(graph_config, title=title)


    def _generate(self):
        positions = range(1, len(self.timings_data.columns) + 1)
        plt_return = plt.violinplot(
            self.timings_data,
            positions=positions,
            showmeans=self.showmeans,
            showextrema=self.showextrema,
        )
        plt_return["bodies"][0].set_facecolor(self.CYTHON_LEGEND_COLOR)
        plt_return["bodies"][1].set_facecolor(self.NUMPY_LEGEND_COLOR)

        plt.xticks(positions, self.timings_data.columns)
        plt.legend(self.timings_data.columns, loc=self.loc)


class LinePlot(BaseGraph):
    """Classe usada para gerar gráficos de linha."""

    def _generate(self):
        plt_return = plt.plot(self.timings_data)
        plt_return[0].set_color(self.CYTHON_LEGEND_COLOR)
        plt_return[1].set_color(self.NUMPY_LEGEND_COLOR)

        plt.legend(self.timings_data.columns)
