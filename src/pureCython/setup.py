# compile files: python ./src/pureCython/setup.py build_ext --inplace
# clean files: python ./src/pureCython/setup.py clean --all

import os
from typing import Final

import numpy as np
from Cython.Build import cythonize
from setuptools import setup
from setuptools.extension import Extension

os.chdir("./src/pureCython/")

FOLDER_FILTER: Final[tuple[str]] = ("build", ".", "__pycache__")

CYTHON_FOLDERS: Final[list[str]] = [
    path for path in os.listdir()
    if not any(folder_filter in path for folder_filter in FOLDER_FILTER)
]

print(CYTHON_FOLDERS)

ext_modules = []
for folder in CYTHON_FOLDERS:
    ext_modules.append(
        Extension(
            folder,
            [f"./{folder}/" + "*.pyx"],
            include_dirs=[np.get_include()],
            language="c",
        )
    )

setup(ext_modules=cythonize(ext_modules))
