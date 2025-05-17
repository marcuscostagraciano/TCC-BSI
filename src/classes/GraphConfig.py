from dataclasses import KW_ONLY, dataclass, field

import pandas as pd


@dataclass
class GraphConfig:
    """Classe usada para armazenar as informações necessárias para a geração dos gráficos.
    Args:
            timings_data (pd.DataFrame): DataFrame contendo as medições para a geração dos gráficos.
            loc (str): Local do gráfico onde a legenda deve aparecer.
            grid (bool): Define se a "grid" deve aparecer na impressão do gráfico.
            title (str): Título do gráfico.
            xlabel (str): Legenda do eixo X.
            ylabel (str): Legenda do eixo Y.
    """

    loc: str | None = None
    grid: bool = True
    title: str = ""
    xlabel: str = "Nº de medições"
    ylabel: str = "Tempo (ms)"
    # O parâmetro abaixo força que todos os parâmetros definidos após ele sejam passados apenas como argumentos nomeados (keyword-only).
    _ = KW_ONLY
    # DataFrame contendo os tempos de execução das funções a serem plotadas
    # O parâmetro "field" é utilizado para definir propriedades adicionais do atributo em dataclasses.
    # O argumento "default_factory" especifica uma função que será chamada para fornecer o valor padrão do atributo.
    # Neste caso, "pd.DataFrame" é chamado para garantir que timings_data seja inicializado como um DataFrame vazio por padrão.
    timings_data: pd.DataFrame = field(default_factory=pd.DataFrame)
