# compile files: python ./src/pureCython/setup.py build_ext --inplace
# clean files: python ./src/pureCython/setup.py clean --all

import os
from typing import Final

from Cython.Build import cythonize
from numpy import get_include
from setuptools import setup
from setuptools.extension import Extension

# Altera o diretório para onde estão os módulos Cython
os.chdir("./src/pureCython/")
# Tupla com nomes de pastas que devem ser ignoradas
FOLDER_FILTER: Final[tuple[str]] = ("build", ".", "__pycache__")
# Lista todas as pastas no diretório atual, exceto as que estão em FOLDER_FILTER
CYTHON_FOLDERS: Final[list[str]] = [
    path for path in os.listdir()
    if not any(folder_filter in path for folder_filter in FOLDER_FILTER)
]

print(f"{CYTHON_FOLDERS = }")

# Cria uma lista para armazenar os módulos de extensão
ext_modules: list[Extension] = []
for folder in CYTHON_FOLDERS:
    # Para cada pasta, cria uma extensão Cython
    ext_modules.append(
        Extension(
            # Nome do módulo
            folder,
            # Arquivos fonte .pyx dentro da pasta
            [f"./{folder}/" + "*.pyx"],
            # Inclui diretório de headers do numpy
            include_dirs=[get_include()],
            # Linguagem alvo (C)
            language="c",
        )
    )

# Executa o setup, compilando os módulos Cython encontrados
setup(ext_modules=cythonize(ext_modules))
