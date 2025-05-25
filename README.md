# Análise Comparativa: NumPy x Implementações C/Cython

*Read this in other languages: [English](README.en.md)*

Este projeto visa compararo desempenho de operações estatísticas básicas entre a biblioteca NumPy e implementações personalizadas em C e Cython.

## 🎯 Objetivo

Analisar e comparar o tempo de execução de diferentes operações estatísticas (máximo, mínimo, média e amplitude) implementadas em C puro, Cython e NumPy, utilizando grandes conjuntos de dados.

## 🛠️ Compilação dos Módulos Cython

Para compilar os módulos Cython, utilize o script de setup com interface CLI:

```bash
python setup.py build_ext --inplace
```

Para limpar os arquivos gerados:

```bash
python setup.py clean --all
```

Para ver a ajuda detalhada do setup:

```bash
python setup.py --help-setup
```

### Interface CLI

O script de setup possui uma interface de linha de comando que facilita a compilação e limpeza dos módulos:

- `build_ext`: Compila todos os módulos Cython encontrados em `src/pureCython/`
  - `--inplace`: Compila as extensões no local original dos arquivos
- `clean`: Remove arquivos de compilação
  - `--all`: Remove todos os artefatos de compilação
- `--help-setup`: Exibe ajuda detalhada sobre os comandos disponíveis

## 🏗️ Arquitetura do Projeto

### Estrutura de Classes

#### Classes de CLI

- **CLIHandler**: Classe responsável pela interface de linha de comando
  - Gerencia argumentos e opções do CLI
  - Implementa parser de argumentos customizado
  - Fornece mensagens de ajuda detalhadas
  - Opções para build, clean e help
  - Interface amigável com mensagens em português

#### Classes de Setup

- **SetupConfig**: Classe de configuração para o processo de build
  - Define caminhos do projeto e configurações de build
  - Gerencia filtros de arquivos e diretórios
  - Utiliza dataclass para configuração simplificada
  - Controle de quais arquivos devem ser ignorados
  - Validação de caminhos do projeto

- **CythonSetup**: Classe para gerenciamento da compilação
  - Descobre automaticamente módulos Cython no projeto
  - Gerencia a criação e compilação das extensões
  - Utiliza métodos de classe para operações estáticas
  - Suporte a compilação incremental
  - Gerenciamento automático de dependências

#### Classes de Gráficos

- **GraphConfig**: Classe de configuração para geração de gráficos
  - Armazena configurações como título, legendas, grid e dados
  - Utiliza decorador `@dataclass` para simplificar a gestão de dados

- **BaseGraph**: Classe base para gráficos
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
  - Suporte a execução silenciosa (apenas download)

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

1. Via Python Script:

   ```bash
   python main.py
   ```

1. Via Jupyter Notebook:
   - Abra o arquivo `main.ipynb`
   - Execute as células sequencialmente

### Configurações dos Testes

- `NUM_REPETICOES`: Número de vezes que cada teste é executado
- `NUM_REGISTROS`: Tamanho do array de teste
- As configurações podem ser ajustadas no arquivo `src/utils/consts.py`

### Visualização dos Resultados

Os testes geram automaticamente:

- Gráficos de violino
- Gráficos de linha
- Dados brutos em formato CSV
- Opção de salvar resultados sem exibição

## 📊 Estrutura do Projeto

```markdown
TCC-BSI/
├── src/
│   ├── pureCython/      # Implementações Cython
│   ├── classes/         # Classes de gráficos e setup
│   ├── tests/           # Testes de desempenho
│   └── utils/           # Utilitários
├── main.py              # Script principal
├── main.ipynb          # Notebook Jupyter
└── setup.py            # Script de setup com CLI
```

[<img align="right" alt="Voltar ao topo" src="https://img.shields.io/badge/%E2%86%91-Voltar%20ao%20topo-lightgrey" />](#análise-comparativa-numpy-x-implementações-ccython)
