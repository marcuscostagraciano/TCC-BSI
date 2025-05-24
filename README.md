# Análise Comparativa: NumPy x Implementações C/Cython

Este projeto visa comparar o desempenho de operações estatísticas básicas entre a biblioteca NumPy e implementações personalizadas em C e Cython.

## 🎯 Objetivo

Analisar e comparar o tempo de execução de diferentes operações estatísticas (máximo, mínimo, média e amplitude) implementadas em C puro, Cython e NumPy, utilizando grandes conjuntos de dados.

## 🛠️ Compilação dos Módulos Cython

Para compilar os arquivos Cython, execute:

```bash
python ./src/pureCython/setup.py build_ext --inplace
```

Para limpar os arquivos gerados:

```bash
python ./src/pureCython/setup.py clean --all
```

## 🏗️ Arquitetura do Projeto

### Estrutura de Classes

#### Classes de Gráficos

- **GraphConfig**: Classe de configuração para geração de gráficos
  - Armazena configurações como título, legendas, grid e dados
  - Utiliza decorador `@dataclass` para simplificar a gestão de dados

- **BaseGraph**: Classe abstrata base para gráficos
  - Define interface comum para todos os tipos de gráficos
  - Implementa funcionalidades básicas como configuração e geração

- **Classes Específicas de Gráficos**:
  - `BoxPlot`: Gera gráficos de caixa
  - `ViolinPlot`: Gera gráficos de violino
  - `LinePlot`: Gera gráficos de linha

#### Classes de Testes

- **BaseTests**: Classe base para testes de desempenho
  - Gerencia configurações de download dos gráficos
  - Implementa método genérico para geração de gráficos
  - Permite configurar salvamento automático dos resultados
  - Controla exibição vs. download dos gráficos

- **Tests**: Classe principal de testes que herda de BaseTests
  - Mantém cache dos resultados NumPy para reuso
  - Implementa testes específicos para cada operação:
    - Valor máximo (C e Cython)
    - Valor mínimo (C e Cython)
    - Média aritmética (Cython)
    - Amplitude (C e Cython)
  - Oferece métodos para execução:
    - Individual: por tipo de operação
    - Completa: todas as operações sequencialmente
  - Permite encadeamento de métodos (method chaining)

### Testes de Desempenho

Os testes comparam as seguintes operações:

- Valor Máximo (C e Cython vs NumPy)
- Valor Mínimo (C e Cython vs NumPy)
- Média Aritmética (Cython vs NumPy)
- Amplitude (C e Cython vs NumPy)

## ⚡ Executando os Testes

### Pré-requisitos

- Python 3.10+
- NumPy
- Matplotlib
- Pandas
- Cython

### Instalação

```bash
pip install -r requirements.txt
```

### Execução

1. **Via Python Script**:

```bash
python main.py
```

2. **Via Jupyter Notebook**:

- Abra o arquivo `main.ipynb`
- Execute as células sequencialmente

### Configurações dos Testes

- `NUM_REPETICOES`: Número de vezes que cada teste é executado
- `NUM_REGISTROS`: Tamanho do array de teste
- As configurações podem ser ajustadas no arquivo `src/utils/consts.py`

### Visualização dos Resultados

Os testes geram automaticamente:

- Gráficos de violino para distribuição dos tempos
- Gráficos de linha para análise temporal
- Opção de salvar gráficos em disco via método `download()`

## 📊 Estrutura do Projeto

```markdown
TCC-BSI/
├── src/
│   ├── pureCython/      # Implementações Cython
│   ├── classes/         # Classes de gráficos
│   ├── tests/           # Testes de desempenho
│   └── utils/           # Utilitários
├── main.py              # Script principal
└── main.ipynb           # Notebook Jupyter
└── setup.py             # Script de setup
```
