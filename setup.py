# compile files: python setup.py build_ext --inplace
# clean files: python setup.py clean --all

import os
from pathlib import Path
from typing import Final

from Cython.Build import cythonize
from numpy import get_include
from setuptools import setup
from setuptools.extension import Extension

# Define caminhos base
PROJECT_ROOT = Path(__file__).parent
CYTHON_ROOT = PROJECT_ROOT / "src" / "pureCython"

# Tupla com nomes de pastas que devem ser ignoradas
FOLDER_FILTER: Final[tuple[str]] = ("build", ".", "__pycache__")

# Lista todas as pastas no diretório Cython, exceto as que estão em FOLDER_FILTER
CYTHON_FOLDERS: Final[list[str]] = [
    path for path in os.listdir(CYTHON_ROOT)
    if not any(folder_filter in path for folder_filter in FOLDER_FILTER)
]

print(f"{CYTHON_FOLDERS = }")

# Cria uma lista para armazenar os módulos de extensão
ext_modules: list[Extension] = []
for folder in CYTHON_FOLDERS:
    # Para cada pasta, cria uma extensão Cython
    ext_modules.append(
        Extension(
            # Nome do módulo completo
            f"src.pureCython.{folder}",
            # Arquivos fonte .pyx dentro da pasta
            [str(CYTHON_ROOT / folder / "*.pyx")],
            # Inclui diretório de headers do numpy
            include_dirs=[get_include()],
            # Linguagem alvo (C)
            language="c",
        )
    )

# Executa o setup, compilando os módulos Cython encontrados
setup(ext_modules=cythonize(ext_modules))
