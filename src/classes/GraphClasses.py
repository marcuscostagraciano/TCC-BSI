import os
from abc import ABC, abstractmethod
from typing import Final, Self
from uuid import uuid4

import matplotlib.pyplot as plt

from . import GraphConfig


class BaseGraph(ABC):
    """Classe base para geração de gráficos."""

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

    def generate(self):
        """Função usada como "wrapper" de outras funções essenciais para geração dos gráficos."""
        self.__setGraphInfo()
        self._generate()
        plt.show()


    def download(self, download_folder: str) -> None:
        """Função usada para salvar o gráfico gerado.

        Args:
                download_folder (str): Caminho onde o gráfico será salvo.
        """

        # Verifica se o diretório existe, caso contrário, cria
        os.makedirs(download_folder, exist_ok=True)

        self.__setGraphInfo()
        self._generate()
        plt.savefig(f"{download_folder}/{self.title} - {uuid4()}.png")


    @abstractmethod
    def _generate(self):
        """Essa função deve ser implementada em cada classe, para definir o tipo de gráfico usado e suas propriedades."""
        pass


class Boxplot(BaseGraph):
    """Classe usada para gerar gráficos de caixa."""

    def __init__(
        self: Self,
        graph_config: GraphConfig,
        title: str | None = None,
    ) -> None:
        """Função usada para instanciar um objeto da classe específica.

        Args:
                self (Self): Parâmetro passado automaticamente referente ao objeto sendo instanciado.
                graph_config (GraphConfig): Objeto contendo as informações necessárias para a geração do gráfico.
                title (str | None): Se passado, sobrescreve o título do graph_config.
        """
        super().__init__(graph_config, title=title)

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
        plt_return = plt.violinplot(
            self.timings_data,
            showmeans=self.showmeans,
            showextrema=self.showextrema,
        )
        plt_return["bodies"][0].set_facecolor("#64a4cc")
        plt_return["bodies"][1].set_facecolor("#fb9130")

        plt.legend(self.timings_data.columns)


class LinePlot(BaseGraph):
    """Classe usada para gerar gráficos de linha."""

    def __init__(
        self: Self,
        graph_config: GraphConfig,
        *,
        title: str | None = None,
    ) -> None:
        """Função usada para instanciar um objeto da classe específica.

        Args:
                self (Self): Parâmetro passado automaticamente referente ao objeto sendo instanciado.
                graph_config (GraphConfig): Objeto contendo as informações necessárias para a geração do gráfico.
                title (str | None): Se passado, sobrescreve o título do graph_config.
        """
        super().__init__(graph_config, title=title)

    def _generate(self):
        plt.plot(self.timings_data)
        plt.legend(self.timings_data.columns)
